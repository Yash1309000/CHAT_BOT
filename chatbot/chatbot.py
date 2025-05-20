import random
import json
import pickle
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

def tokenize_and_stem(sentence):
    tokens = word_tokenize(sentence.lower())
    stemmed = [stemmer.stem(word) for word in tokens]
    return ' '.join(stemmed)

class Chatbot:
    def __init__(self):
        # Load model, vectorizer, and intents
        with open('model.pkl', 'rb') as f:
            self.model = pickle.load(f)
        with open('vectorizer.pkl', 'rb') as f:
            self.vectorizer = pickle.load(f)
        with open('intents.json') as f:
            self.intents = json.load(f)

    def get_response(self, sentence):
        sentence_stem = tokenize_and_stem(sentence)
        X = self.vectorizer.transform([sentence_stem])
        pred = self.model.predict(X)[0]

        for intent in self.intents['intents']:
            if intent['tag'] == pred:
                return random.choice(intent['responses'])

        return "Sorry, I didn't understand that. Could you please rephrase?"

# For testing without GUI:
# if __name__ == "__main__":
#     bot = Chatbot()
#     while True:
#         user_input = input("You: ")
#         print("Bot:", bot.get_response(user_input))
