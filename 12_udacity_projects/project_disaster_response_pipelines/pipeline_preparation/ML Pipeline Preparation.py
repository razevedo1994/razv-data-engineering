#!/usr/bin/env python
# coding: utf-8

# # ML Pipeline Preparation
# Follow the instructions below to help you create your ML pipeline.
# ### 1. Import libraries and load data from database.
# - Import Python libraries
# - Load dataset from database with [`read_sql_table`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_sql_table.html)
# - Define feature and target variables X and Y

# In[66]:


import nltk
nltk.download(['punkt', 'wordnet'])


# In[67]:


# import libraries
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


# In[68]:


# load data from database
engine = create_engine('sqlite:///DisasterResponse.db')
df = pd.read_sql("SELECT * FROM final", engine)
X = df['message']
y = df.iloc[:,4:]


# ### 2. Write a tokenization function to process your text data

# In[69]:


text_regex = '[^a-zA-Z0-9]'

def tokenize(text):
    # remove punctuation
    text = re.sub(text_regex, ' ', text)
        
    # tokenize text
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    
    # remove stop words
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok, pos='n').lower().strip()
        clean_tok = lemmatizer.lemmatize(clean_tok, pos='v')
        clean_tokens.append(clean_tok)
        
    return clean_tokens


# ### 3. Build a machine learning pipeline
# This machine pipeline should take in the `message` column as input and output classification results on the other 36 categories in the dataset. You may find the [MultiOutputClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html) helpful for predicting multiple target variables.

# In[70]:


pipeline = Pipeline([
    ('vect', CountVectorizer(tokenizer=tokenize)),
    ('tfidf', TfidfTransformer()),
    ('clf', MultiOutputClassifier(RandomForestClassifier()))
])


# ### 4. Train pipeline
# - Split data into train and test sets
# - Train pipeline

# In[71]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)
y_pred


# ### 5. Test your model
# Report the f1 score, precision and recall for each output category of the dataset. You can do this by iterating through the columns and calling sklearn's `classification_report` on each.

# In[72]:


target_names = y.columns
print(classification_report(y_test, y_pred, target_names=target_names))


# ### 6. Improve your model
# Use grid search to find better parameters. 

# In[ ]:


pipeline.get_params()

parameters = {'tfidf__norm': ['l1','l2'],
              'clf__estimator__criterion': ["gini", "entropy"]
             }

cv = GridSearchCV(pipeline, param_grid=parameters)


# ### 7. Test your model
# Show the accuracy, precision, and recall of the tuned model.  
# 
# Since this project focuses on code quality, process, and  pipelines, there is no minimum performance metric needed to pass. However, make sure to fine tune your models for accuracy, precision and recall to make your project stand out - especially for your portfolio!

# In[ ]:


cv.fit(X_train, y_train)
y_pred = cv.predict(X_test)


# ### 8. Try improving your model further. Here are a few ideas:
# * try other machine learning algorithms
# * add other features besides the TF-IDF

# In[ ]:


target_names = y.columns
print(classification_report(y_test, y_pred, target_names=target_names))


# ### 9. Export your model as a pickle file

# In[ ]:


with open('MLclassifier.pkl', 'wb') as file:
    pickle.dump(cv, file)


# In[ ]:


cv.grid_scores_


# In[ ]:


cv.best_estimator_


# ### 10. Use this notebook to complete `train.py`
# Use the template file attached in the Resources folder to write a script that runs the steps above to create a database and export a model based on a new dataset specified by the user.

# In[ ]:




