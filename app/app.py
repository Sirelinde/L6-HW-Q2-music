 from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from joblib import load
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='')
    else:
        myage = request.form['Your_age']
        mygender = request.form['Your_gender']
        myquali = request.form['Your_quali']
        from sklearn.tree import DecisionTreeClassifier
        df = pd.read_csv("app/music.csv")
        feature_cols = ['age', 'gender', 'academic-qualification']
        x = df[feature_cols]
        y = df.music
        model = DecisionTreeClassifier()
        model = model.fit(x.values, y)
        np_arr = np.array([myage, mygender, myquali])
        y_pred = model.predict([np_arr])  
        y_pred_to_str = str(y_pred)
        #return predictions_to_str
        return render_template('index.html', href2='The suitable music for you (age:'+str(myage)+', gender:'+str(mygender)+', academic qualification:'+str(myquali)+') is:'+y_pred_to_str)

