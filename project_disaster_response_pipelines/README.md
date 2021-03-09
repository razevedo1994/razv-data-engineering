# Disaster Response Classification API


### Project Motivation<a name="Motivation"></a>

The goal of the project is to classify the disaster messages into categories. In this project, I analyzed disaster data from [Figure Eight](https://appen.com/) to build a model for an API that classifies disaster messages. Through a web app, the user can input a new message and get classification results in several categories. The web app also display visualizations of the data.

### Project Descriptions<a name="Description"></a>

The project has three componants which are:

#### ETL Pipeline: [process_data.py](https://github.com/Suveesh/Disaster-Response-Pipeline/blob/main/data/process_data.py) file contain the script to create ETL pipline which:

- [x] Loads the messages and categories datasets.
- [x] Merges the two datasets
- [x] Cleans the data
- [x] Stores it in a SQLite database

#### ML Pipeline: [train_classifier.py](https://github.com/Suveesh/Disaster-Response-Pipeline/blob/main/model/train_classifier.py) file contain the script to create ML pipline which:

- [x] Loads data from the SQLite database
- [x] Splits the dataset into training and test sets
- [x] Builds a text processing and machine learning pipeline
- [x] Trains and tunes a model using GridSearchCV
- [x] Outputs results on the test set
- [x] Exports the final model as a pickle file

#### Flask Web App: the web app enables the user to enter a disaster message, and then view the categories of the message.

- [x] The web app also contains some visualizations that describe the data.
