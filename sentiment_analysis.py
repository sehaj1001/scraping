'''
Sehajpreet Kaur
Aditi KP
Sejal Bansal

Used NLTK VADER sentiment analysis
'''

#import librarires
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import csv

filename = "Singapore\Park Regis.csv"
rows = []
comments = []  # to store the comments in a list
with open(filename, 'r', encoding="utf8") as csvfile:  # reading the csv file to get the comments
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)

for row in rows[1:121]:  # first row is headings; 120 comments for each hotel
    for col in row:
        comments.append(col)  # only need to append the comments column and not the rating
        break

s = SentimentIntensityAnalyzer()
for comment in comments:  # for each comment in list if comments
    score = s.polarity_scores(comment)  # calculate polarity score
    print(score['compound'])  # compound is the final polarity score after calculating positive, negative and neutral
