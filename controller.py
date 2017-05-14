#!/usr/bin/env python3

from flask import (Flask,render_template,request,flash,url_for,session)

import models 

app = Flask(__name__)


app.config["SECRET_KEY"] = open("SECRET_KEY", "rb").read()

# Frontpage
@app.route('/')
def serve_frontpage():
    tweets = models.Tweet.publ()
    return render_template('index.html', latest_tweets=tweets)
    #latest_tweets to be used in dynamic html

# Register
@app.route('/serve-register')
def serve_register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    username=session['username']
    tweets=models.Tweet.priv(username)
    return render_template('dashboard.html', username=username, user_tweets=tweets)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/check-credentials-register', methods=["POST"])
def check_credentials_register():
    __username = request.form['username']
    __password = request.form['password']
#   We are skipping at least two important cybersec. practices:
#       1) We're not hashing the inputs
#       2) We're not evaluating against None or null
#       3) We're not checking a database-- this is hard coded
    result = models.User.register(__username, __password)
    if result == False:
        flash('that username already exists, please login.')
        return serve_login()
    else:
        return dashboard()

# Welcome
# @app.route('/serve-welcome')
# def serve_welcome():
#     return render_template('welcome.html')


# Login
@app.route('/serve-login')
def serve_login():
    return render_template('login.html')


@app.route('/check-credentials-login', methods=["POST"])
def check_credentials_login():
    __username = request.form['username']
    __password = request.form['password']
#   We are skipping at least two important cybersec. practices:
#       1) We're not hashing the inputs
#       2) We're not evaluating against None or null
#       3) We're not checking a database-- this is hard codedresult = models.User.register(__username, __password)
    result = models.User.login(__username, __password)
    if result == False:
        flash('incorrect login, try again')
        return serve_login()
    else:
        session['username']=__username
        tweets=models.Tweet.priv(__username)
        return dashboard()
        # render_template('dashboard.html', user_tweets=tweets, username=__username)

@app.route('/tweet', methods=["POST"])
def tweet():
    __tweet = request.form['twttr'] # from html form name, __tweet is a string from user form
    # print(__tweet)
    username = session['username']
    user_id = models.User.get_id(username)
    models.Tweet.store_tweet(__tweet, user_id)
    return dashboard()




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)