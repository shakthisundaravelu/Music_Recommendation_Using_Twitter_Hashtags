import json
from flask import Flask, render_template, request,send_from_directory,url_for,redirect,session
import fetchTwitter as ft
from sklearn.externals import joblib
from nltk.tokenize import TweetTokenizer


app = Flask(__name__)
app.secret_key = 'any random string'

def tokenize(text):
    tknzr = TweetTokenizer()
    return tknzr.tokenize(text)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search',methods=['POST','GET'])
def search():
    if request.method == 'POST':
        ss =request.form.get('query')
        tweets= ft.search_tweet(ss)
        # print(tweets)
        session['tweets'] = tweets
        
        return render_template("result.html",tweets=tweets)
    else:
        return render_template('index.html')


@app.route('/getRec',methods=['POST'])
def getrec():
    tweets= session['tweets']
    import testReco as tr
    id=request.form.get('id')
    print(id)
    
    
    ss =tr.get_recom([tweets[int(id)]])
    #print(ss)
    aa=[]
    for i in ss:
        aa.append(i)
    return json.dumps(aa);


@app.route('/getDirectRec',methods=['POST'])
def getRecDirect():
    tweet =request.form.get('tweet')
    print("the tweet is")
    print( tweet)
    import testReco as tr
    ss =tr.get_recom([tweet])
    print(ss)
    aa=[]
    for i in ss:
        aa.append(i)
    return json.dumps(aa);

if __name__ == '__main__':
   app.run(debug = True)
