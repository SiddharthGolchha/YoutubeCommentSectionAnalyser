# YoutubeCommentSectionAnalyser
This Python script performs sentiment analysis on the comments of a YouTube video using the YouTube Data API and the Sentiment Intensity Analyzer from NLTK library. It also calculates the frequency distribution of the words in the comments.

# Prerequisites:

Libraries: requests, beautifulsoup4, nltk, textblob.
Google API Key: Required for accessing the YouTube Data API.
# Usage:

Set your Google API key in the api_key variable.
Replace video_id with the ID of the YouTube video you want to analyze.
Run the script (python youtube_comment_sentiment_analysis.py).
# How it works:
Fetches comments (max 100) from the specified video through the YouTube Data API.
Analyzes each comment's sentiment using TextBlob (Positive, Neutral, Negative).
Creates a word frequency distribution using NLTK's SentimentIntensityAnalyzer.
Prints the 10 most common words and the overall sentiment score.
# Note:
The script retrieves a maximum of 100 comments due to the maxResults parameter. See commented section for fetching more.
Feel free to modify the script for different scenarios and video IDs.
# Additional Information:
This is a basic script and can be enhanced with features like filtering comments based on specific criteria, analyzing specific emotions, or visualizing results.
Explore resources like NLTK and TextBlob documentation for advanced functionalities.
