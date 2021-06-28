import nltk
nltk.download('stopwords')
nltk.download('wordnet')
import re
import six.moves.cPickle as pickle
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Function to input Raw Text
def getRawText():
	print("Input a paragraph whose sentiments is to be analyzed :\n")
	raw_text = input()
	if raw_text == '' :
		exit()
	else :
		return raw_text

# Removal of all Special Characters
def removeSpecialChars(text):
	return re.sub('[^a-zA-Z]', ' ', text)

# Removal of Alpha-Numeric Words
def removeAlphaNumericWords(text):
	return re.sub("\S*\d\S*", "", text).strip()

# TEXT PREPROCESSING/CLEANING Function
def doTextCleaning(text):
	text = removeSpecialChars(removeAlphaNumericWords(text)).lower().split()

	# Stopwords Removal and Lemmatization
	lmtzr = WordNetLemmatizer()
	text = [lmtzr.lemmatize(word, 'v') for word in text if word not in set(stopwords.words('english'))]
	
	text = " ".join(text)
	return text

def getScore(text):
	# Loading train.pkl
	f = open('C:/Users/pc/Desktop/TCS RIO 45/train.pkl', 'rb')
	train = pickle.load(f)
	f.close()
	
	X_test = [text]
	vectorizer = CountVectorizer() #Creating an instance of CountVectorizer
	train_features = vectorizer.fit_transform([t for t in train[0]]) #Vectorization of trained model
	Xt_vec = vectorizer.transform(X_test).toarray() #Vectorization of X_test
	mn = MultinomialNB() #Creating an instance of Multinomial Naïve Bayes
	mn.fit(train_features, [int(t) for t in train[1]]) #Fitting Trained model into the instance of Multinomial Naïve Bayes
	y_pred = mn.predict(Xt_vec) #Getting Score
	return y_pred

def main():
	raw_text = getRawText() #Calling Function to get Raw Paragraph Input
	cleaned_text = doTextCleaning(raw_text) #Calling Test Cleaning Function
	# print(cleaned_text)
	score = getScore(cleaned_text) # Calling Score Calculation Function
	if score == 1 :
		print("Positive")
	elif score == 0 :
		print("Negative")
	else :
		print("Neutral")

if __name__ == '__main__':
	main()
