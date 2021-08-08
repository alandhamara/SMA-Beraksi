import numpy as np
import pandas as pd
import functools
import itertools
from sklearn.feature_extraction.text import TfidfVectorizer

def fungsipertama(text):
 
  lol = pd.read_csv('semangatkawan (1).csv', delimiter=';')
  lol.tail()

  X = lol.iloc[:,0].values
  y = lol.iloc[:,1].values

  X[20:]
  
  tfidfvectorizer = TfidfVectorizer(max_features=100000, use_idf=True)
  tfidfvectorizer.fit(X[:30])
  X_train = tfidfvectorizer.transform(X[:30])
  X_test = tfidfvectorizer.transform(X[30:])
  y_train = y[:30]
  y_test = y[30:]

  X[1]
  text_coba = str(text)
  coba = tfidfvectorizer.transform([text_coba]).todense()

  cobaa = coba.tolist()

  features = tfidfvectorizer.get_feature_names()

  aku = []
  kata = []

  for i in range(len(cobaa[0])):
      if cobaa[0][i] != 0.0:
          hahaha = cobaa[0][i]
          aku.append(hahaha)

  for i in range(len(cobaa[0])):
      if cobaa[0][i] != 0.0:
          haha = features[i]
          kata.append(haha)
    # Converting to list
  zipped = zip(aku, kata)
  zipped = list(zipped)
  
    # Printing zipped list
    # print("Initial zipped list - ", str(zipped))
  
    # Using sorted and lambda
  katapenting = sorted(zipped, key = lambda x: x[0],reverse=True)
      
    # printing result
    # print("final list - ", str(res))
  hasil = str(katapenting[:5])

  return hasil
  