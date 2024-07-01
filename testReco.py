import pandas as pd
from textblob import TextBlob
import requests
import json
from musicreco import getRecommendations

from sklearn.externals import joblib
from nltk.tokenize import TweetTokenizer

def tokenize(text):
    tknzr = TweetTokenizer()
    return tknzr.tokenize(text)


grid_svm = joblib.load('clfgenre.pkl')

def get_recom(tweet):
    try:
        payload = {'sentence' : tweet[0]}
        r = requests.get('http://www.thesarcasmdetector.com/_compute', params=payload)
        stri = r.content
        jsonobj = json.loads(stri)
        sarscore = jsonobj['result']
        
        res = TextBlob(tweet[0]).sentiment.polarity
        if  res > 0:
            if(sarscore<0):
                tweet[0]+=" Positive"
            else:
                tweet[0]+= " Negative"
        elif res <0 :
            if(sarscore<0):
               tweet[0]+= " Negative"
            else:
                tweet[0]+= " Positive"
        else:
            tweet[0]+= " Neutral"


    except:
        return tweet[0]
    print(tweet)
    a = grid_svm.predict(tweet)
    print(a)
    song = getRecommendations(a)
    print(song)
    return song;

