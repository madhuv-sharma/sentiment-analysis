from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import csv
import re


def getRawText():
	while True:
		print("Input a paragraph whose sentiments is to be analyzed :\n")
		raw_text = input()
		if raw_text == '' :
			print('Invalid Entry')
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
	text = [lmtzr.lemmatize(word, 'v') for word in text if word not in set(stopwords.words('english'))]
	
	text = " ".join(text)
	return text


def main():
	with open(r"C:\Users\pc\Desktop\TCS RIO 45\negative.csv", 'r') as csv_file, open(r"C:\Users\pc\Desktop\output.csv", 'w', newline="") as f_out:
		csv_reader = csv.reader(csv_file, delimiter=',');
		csv_writer = csv.writer(f_out, delimiter=',');
		temp=""
		for row in csv_reader:
			row[0]=doTextCleaning(row[0])
			if row[0]==temp:
				continue
			print(row)
			temp=row[0]
			csv_writer.writerow(row)


if __name__ == '__main__':
	main()
