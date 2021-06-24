import nltk
nltk.download('stopwords')
nltk.download('wordnet')
import re
import six.moves.cPickle as pickle
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def getRawText():
	while True:
		print("Input a paragraph whose sentiments is to be analyzed :\n")
		raw_text = input()
		if raw_text == '' :
			exit()
		else :
			return raw_text

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
	f = open('C:/Users/pc/Desktop/TCS RIO 45/train.pkl', 'rb')
	train = pickle.load(f)
	f.close()
	X_test=[text]
	vectorizer = CountVectorizer()
	train_features = vectorizer.fit_transform([t for t in train[0]])
	Xt_vec = vectorizer.transform(X_test).toarray()
	mn = MultinomialNB()
	#mn.fit(X_vec, y_train)
	mn.fit(train_features, [int(t) for t in train[1]])
	#y_pred = mn.predict(text_vec)
	y_pred = mn.predict(Xt_vec)
	return y_pred

def main():
	raw_text = getRawText()
	cleaned_text = doTextCleaning(raw_text)
	print(cleaned_text)
	score = getScore(cleaned_text)
	if score == 1 :
		print("Positive")
	elif score == 0 :
		print("Negative")
	else :
		print("Neutral")

if __name__ == '__main__':
	main()
