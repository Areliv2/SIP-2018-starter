'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()


# Continue your program below! 
tweettext = []
tweetstring = ""
for tweet in tweetData:
    tweetstring += tweet['text']
    #blob = TextBlob(tweet["text"])
    #tweettext.append(blob)
    #print(tweetstring)

my_list = [1,2,3,4,5,6]  
print(sum(my_list)/ len(my_list)) 

tweetBlob = TextBlob(tweetstring)
print(tweetBlob.translate(to='es'))



blob_polarity = []
for blob in tweettext:
    blob_polarity.append(blob.polarity)

word_dict= {}
'FilteredWord[word] = count'

for word in tweetBlob.words:
    word_dict[word.lower()] = tweetBlob.word_counts[word.lower()]

blob_subjectivity = []
for blob in tweettext:
    blob_subjectivity.append(blob.subjectivity)
    
print(word_dict) 


# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
