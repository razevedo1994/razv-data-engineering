import sys
import pandas as pd
import re
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    
    """
    
    Function to load Messages and Categories Data set from the csv file and merge  
    into a single data frame named df variable
    
    Input: messages_filepath, categories_filepath
    Output: Merged dataframe of messages and categories dataframe
        
    """
    
    # - load messages and categories dataset.
    # - Merge the messages and categories datasets using the common id.
    
    df_messages = pd.read_csv(messages_filepath)
    df_categories = pd.read_csv(categories_filepath)
    df = pd.merge(df_messages, df_categories, how = 'inner', on = 'id')
    
    return df


def clean_data(df):
    
    """
    
    Function to clean the dataset for application use.
    
    Input: df
    Output: cleaned and formatted dataframe
    
    """
    
    # - Split `categories` into separate category columns.
    # - Split the values in the `categories` column on the `;` character so that each value becomes a separate column.
    # - Use the first row of categories dataframe to create column names for the categories data.
    # - Rename columns of `categories` with new column names.
    # - Drop duplicates.
    
    categories = df['categories'].str.split(";", expand = True)
    row = categories.iloc[0].str.split('-', expand = True)
    category_colnames = list(row[0])
    categories.columns = category_colnames
    
    # - Convert category values to just numbers 0 or 1.
    # - Iterate through the category columns in df to keep only the last character of each string (the 1 or 0).
    for column in categories:
        categories[column] = categories[column].str.split('-').str.get(-1)
        categories[column] = categories[column].astype(int)
        
        for n, i in enumerate(categories[column]):
            if i > 1:
                categories[column][n] = 1
        
    # - Drop the original categories column from `df`.
    # - Concatenate the original dataframe with the new `categories` dataframe.
    # - Drop duplicates.
    
    df.drop(['categories'], axis = 1, inplace = True)
    df = pd.concat([df, categories], axis = 1, join = "inner").drop_duplicates()
    
    
    return df
    

def save_data(df, database_filename):
    
    """
    Function to save the cleaned dataframe into a sql database with file name 'message_disaster'
    
    Input: df, database_filename
    Output: SQL Database 
    
    """
    engine = create_engine('sqlite:///'+ database_filename)
    df.to_sql('message_disaster', engine, index=False, if_exists = 'replace')

def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()