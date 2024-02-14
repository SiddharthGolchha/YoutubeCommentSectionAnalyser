import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import requests
from textblob import TextBlob
# API key
api_key = 'Your Google API Key'
com=[]
# API endpoint
url = 'https://www.googleapis.com/youtube/v3/commentThreads'


# Video ID
video_id = 'video id'

# Parameters
params = {
    'key': api_key,
    'part': 'snippet',
    'videoId': video_id,
    'textFormat': 'plainText',
    'maxResults': 100
}

# Send GET request
response = requests.get(url, params=params)

# Extract comments from the response
comments = response.json()['items']

# get the token for next page
next_page_token = response.json().get("nextPageToken", None)


try:
    while next_page_token:
        params['pageToken'] = next_page_token
        # Send GET request
        response = requests.get(url, params=params)
        # Extract comments from the response
        comments += response.json()['items']
        # get the token for next page
        next_page_token = response.json().get("nextPageToken", None)
        print(next_page_token)


except:
    print('Done Scrapping')

# Perform sentiment analysis on the comments
for comment in comments:
    text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        print(text, ": Positive")
    elif analysis.sentiment.polarity == 0:
        print(text, ": Neutral")
    else:
        print(text, ": Negative")
    com.append(text)


print(len(com))
# create a sentiment analyzer
sia = SentimentIntensityAnalyzer()

# join all the articles text in one text
article_text = ' '.join(com)
# tokenize the text
tokens = word_tokenize(article_text)

# remove stop words
stop_words = nltk.corpus.stopwords.words('english')
tokens = [token for token in tokens if token.lower() not in stop_words]

# calculate the frequency distribution of the tokens
fdist = FreqDist(tokens)

# print the 10 most common words
print("10 most common words:")
print(fdist.most_common(10))

# calculate the sentiment of the text
sentiment = sia.polarity_scores(article_text)

# print the overall sentiment
print("Overall sentiment:")
print(sentiment)
