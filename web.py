from flask import Flask,render_template,request,redirect,url_for
import pandas as pd
import numpy as np


app = Flask(__name__)
app.debug=True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/demonstration',methods=["GET", "POST"])
def demonstration():
    if request.method == 'POST':
        print("hh")
        target_name = request.form.get('targetname')
        print(target_name)
        return render_template('1.html',target_name=target_name)
    return render_template('1.html')


@app.route('/demonstration/<targetname>')
def demon(target_name):
    return render_template('1.html',target_name=target_name)


@app.route('/upload')
def upload():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)

