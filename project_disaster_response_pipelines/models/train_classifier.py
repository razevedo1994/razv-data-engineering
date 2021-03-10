# - Import libraries.

import sys
import nltk
nltk.download(['punkt', 'wordnet'])
import re
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sqlalchemy import create_engine
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pickle


def load_data(database_filepath):
    
    """
    Function for loading the database
    
    Input: Databased filepath
    Output: Returns the Features X & target y along with target columns names catgeory_names
    
    """
    engine = create_engine('sqlite:///'+ database_filepath)
    df = pd.read_sql("SELECT * FROM message_disaster", engine)
    
    X = df['message']
    Y = df.iloc[:,4:]
    
    category_names = Y.columns.values
    
    return X, Y, category_names

def tokenize(text):
    
    """
    A tokenization function to process and clean your text data
    
    Input: text
    Output: cleaned tokenized text as a list object
    
    """
    # - Remove punctuation.
    # - Tokenize text.
    # - Remove stop words.
    
    text_regex = '[^a-zA-Z0-9]'
    text = re.sub(text_regex, ' ', text)
        
   
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    
    
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok, pos='n').lower().strip()
        clean_tok = lemmatizer.lemmatize(clean_tok, pos='v')
        clean_tokens.append(clean_tok)
        
    return clean_tokens


def build_model():
    
    """
    Function to build a model and create a pipeline
    
    Input: None
    Output: Returns the model
    
    """
    pipeline = Pipeline([
    ('vect', CountVectorizer(tokenizer=tokenize)),
    ('tfidf', TfidfTransformer()),
    ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])
    
    parameters = {'tfidf__norm': ['l1','l2'],
              'clf__estimator__criterion': ["gini", "entropy"]
             }

    cv = GridSearchCV(pipeline, param_grid=parameters)
    
    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    
    """
    Function to evaluate a model and return the classificatio and accurancy
    
    Inputs: Model, X_test, y_test, Catgegory_names
    Outputs: Prints the Classification report & Accuracy Score
    
    """
    Y_pred = model.predict(X_test)
    report= classification_report(Y_pred,Y_test, target_names=category_names)


    temp=[]
    for item in report.split("\n"):
        temp.append(item.strip().split('     '))
    clean_list=[ele for ele in temp if ele != ['']]
    report_df=pd.DataFrame(clean_list[1:],columns=['group','precision','recall', 'f1-score','support'])


    return report


def save_model(model, model_filepath):
    
    """
    Export your model as a pickle file
    
    Input: model and the file path to save the model
    Output: save the model as pickle file in the give filepath 
    
    """
    with open(model_filepath, 'wb') as file:
        pickle.dump(model, file)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()