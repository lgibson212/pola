#!/usr/bin/env python3

from flask import (Flask,render_template,request,flash,url_for,session)

# import models 

app = Flask(__name__)

# app.config["SECRET_KEY"] = open("SECRET_KEY", "rb").read()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/wakeup')
def wakeup():
    return render_template('wakeup.html')

@app.route('/feel')
def feel():
    return render_template('feel.html')

@app.route('/photo')
def photo():
    return render_template('photo.html')

@app.route('/photo-gallery')
def photo_gallery():
    return render_template('photo_gallery.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/thinking')
def thinking():
    return render_template('thinking.html')

@app.route('/med-check')
def med_check():
    return render_template('med_check.html')

@app.route('/took-meds')
def took_meds():
    return render_template('took_meds.html')

@app.route('/forgot_meds')
def forgot_meds():
    return render_template('forgot_meds.html')

@app.route('/rest')
def rest():
    return render_template('rest.html')

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/demo')
def demo():
    return render_template('chart1.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)