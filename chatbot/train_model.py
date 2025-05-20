
import json
import random
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import nltk
from nltk.stem.porter import PorterStemmer

nltk.download('punkt')

stemmer = PorterStemmer()

def tokenize_and_stem(sentence):
    from nltk.tokenize import word_tokenize
    tokens = word_tokenize(sentence.lower())
    stemmed = [stemmer.stem(word) for word in tokens]
    return ' '.join(stemmed)

# Load intents
with open('intents.json') as f:
    data = json.load(f)

X = []
y = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        X.append(tokenize_and_stem(pattern))
        y.append(intent['tag'])

# Vectorize text
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train classifier
clf = LogisticRegression()
clf.fit(X_vec, y)

# Save model and vectorizer
with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Model training complete and saved.")
