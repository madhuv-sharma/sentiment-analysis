import nltk
# nltk.download('stopwords')
# nltk.download('wordnet')
#import numpy as np
#import pandas as pd
import re
#import spacy
#from nltk import NaiveBayesClassifier as nbc
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
#from sklearn.preprocessing import LabelEncoder

def getRawText():
	while True:
		print("Input a paragraph whose sentiments is to be analyzed :\n")
		raw_text = input()
		if raw_text == '' :
			print('Invalid Entry')
		else :
			return raw_text

'''
def removeApostrophe(text):
	phrase = re.sub(r"won't", "will not", text)
	phrase = re.sub(r"can\'t", "can not", text)
	phrase = re.sub(r"n\'t", " not", text)
	phrase = re.sub(r"\'re", " are", text)
	phrase = re.sub(r"\'s", " is", text)
	phrase = re.sub(r"\'d", " would", text)
	phrase = re.sub(r"\'ll", " will", text)
	phrase = re.sub(r"\'t", " not", text)
	phrase = re.sub(r"\'ve", " have", text)
	phrase = re.sub(r"\'m", " am", text)
	return phrase
'''

def removeSpecialChars(text):
	return re.sub('[^a-zA-Z]', ' ', text)

def removeAlphaNumericWords(text):
	return re.sub("\S*\d\S*", "", text).strip()

def doTextCleaning(text):
	text = removeSpecialChars(removeAlphaNumericWords(text)).lower().split()

	#Removing Stopwords and Lemmatization
	lmtzr = WordNetLemmatizer()
	text = [lmtzr.lemmatize(word, 'v') for word in text if not word in set(stopwords.words('english'))]
	
	text = " ".join(text)
	return text

def getScore(text):
	X_train = []
	y_train = []
	mn = MultinomialNB()
	mn.fit(X_vec, y_train)
	y_pred = mn.predict(text)
	return y_pred

def main():
	raw_text = getRawText()
	print(raw_text)
	cleaned_text = doTextCleaning(raw_text)
	print(cleaned_text)
	score = getScore(cleaned_text)
	if score == 4 :
		print("Positive")
	elif score == 0 :
		print("Negative")
	else :
		print("Neutral")

if __name__ == '__main__':
	main()