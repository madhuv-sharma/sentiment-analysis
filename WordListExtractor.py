import csv
import urllib.request

url="https://ptrckprry.com/course/ssd/data/negative-words.txt"
with open ("C:/Users/pc/Desktop/output.csv", 'w', newline="") as csv_file:
	csv_writer = csv.writer(csv_file, delimiter=',')
	file = urllib.request.urlopen(url)
	for line in file:
		try:
			decoded_line = line.decode("utf-8")
			string=str(decoded_line)
			if string.find(';') == -1:
				row[0]=string.rstrip("\n")
				csv_writer.writerow(row)
				print(row)
			else:
				continue
		except Exception:
			continue