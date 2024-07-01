# Music-Recommendation-Using-Twitter-Hashtags
An App that recommends Music from the given text.
The App can work in two ways
* Staight away give the text to which Music has to be recommended.
* Give the hashtag to fetch all the recent tweets for this hashtag and select from anyone of those tweets to recommend music.
One can tweet something in his twitter account and use the hashtag to find his tweet and get recommended.
### Whats Happening inside the App?
1. The text is analysed to deduct the sentiment from it.
2. Using the deducted Sentiment, the app then predicts the genre for the given tweet and the mood.
3. A song(say X) of that particular genre is selected.
4. Songs that are similar to X in the dataset is ranked in the order of decreasing similarity.
