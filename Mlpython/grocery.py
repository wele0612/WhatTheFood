## for data
import pandas as pd
import numpy as np
import pickle
import nltk
## for plotting
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
## for machine learning
from sklearn import model_selection, preprocessing, feature_selection, ensemble, linear_model, metrics, decomposition
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report
## for explainer
from lime import lime_tabular
from nltk.corpus import stopwords
from sklearn.metrics import accuracy_score

## reading data
data = pd.read_csv(r"C:\Users\lily xie\Downloads\grocery.csv")
print(data)

## data cleaning
for Item in data.columns:
    data[Item] = data[Item].str.lower() 
print(data)

# filtered list
# dataDairy = data[data['label'] == "dairy"]
# print(dataDairy)
# dataMeat = data[data['label'] == "meat"]
# print(dataMeat)
# dataProduce = data[data['label'] == "produce"]
# print(dataProduce)
# dataSeafood = data[data['label'] == "seafood"]
# print(dataSeafood)

categories = ['dairy', 'meat', 'produce', 'seafood']
train, test = train_test_split(data, random_state=42, test_size=0.25, shuffle=True)
X_train = train.label
X_test = test.label
print(X_train.shape)
print(X_test.shape)


## Machine Learning using Naive Bayes Algorithm, Training vs. Testing = 3:1
X = data.item
y = data.label
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 42)

nb = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', MultinomialNB()),
              ])

nb.fit(X_train, y_train)
y_pred = nb.predict(X_test)
print(y_pred.shape)
print(y_test.shape)
print('accuracy %s' % accuracy_score(y_pred, y_test))
## print('Test accuracy is {}'.format(accuracy_score(test[category], prediction)))
print(classification_report(y_test, y_pred))
