from flask import Flask, jsonify
from joblib import load
import pandas as pd

app = Flask(__name__)
model = load('model.joblib') 

@app.route('/')
def welcome():
    return "Welcome to our model!"

@app.route('/<radius>/<area>')
def predict(radius,area):
    df = pd.DataFrame({
        "radius_mean": [radius],
        "area_mean":[area]
    })
    p = model.predict(df)[0]
    print(p)
    if p==1:
        return jsonify(result = "Malignant")
    else:
        return jsonify(result = "benign")





