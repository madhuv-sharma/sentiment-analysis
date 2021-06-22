import nltk
# nltk.download('stopwords')
# nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import re
from nltk import NaiveBayesClassifier as nbc
#import spacy

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
	pos = 
	neg = 
	return (pos, neg, text)

def main():
	raw_text = getRawText()
	print(raw_text)
	cleaned_text = doTextCleaning(raw_text)
	print(cleaned_text)
	pos, neg, x = getScore(cleaned_text)
	print(pos)
	print(neg)
	if pos < 50 and neg < 50 :
		print("Neutral")
	elif pos > neg :
		print("Positive")
	else :
		print("Negative")

if __name__ == '__main__':
	main()