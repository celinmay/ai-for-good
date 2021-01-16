from flask import Flask, jsonify, request, render_template
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf 
import numpy as np
from keras.models import load_model
import pandas as pd
from run_ann import loaded_ann
import csv


app = Flask(__name__)


def fetchSymptoms():
    return {'Fever': 0, 'Cough': 0, 'Problems Breathing': 0}


@app.route("/", methods=['GET'])
def index():
    symptoms = fetchSymptoms()
    return render_template("index.html", symptoms = symptoms)


@app.route("/data", methods=['POST', 'GET'])
def myFunction():
    if request.method == 'POST':
        symptoms = fetchSymptoms()
        symptomsList= request.form.getlist('symptom')

        #for s in symptomsList: 
        for i in range(len(symptomsList)):
    
            symptoms[symptomsList[i]] = 1 

            fieldnames = ['symptom', 'symptom']

        with open('data.csv', 'a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=symptoms.keys())
         
            writer.writerow(symptoms)
            return render_template("index.html", symptoms = symptoms)

@app.route("/results", methods=['GET'])
def results():
    #data = request.get_json(force=True)
    #prediction = model.predict([np.array(list(data.values()))])

  
    return render_template("results.html", predictions=predictions)


# Importing the dataset
dataset = pd.read_csv('data.csv') # Enter dataset
# X
X = dataset.iloc[:,-1]
X = np.array([X], dtype = np.float64)


# Load model 
loaded_ann = keras.models.load_model('Covid_model')

#Trying it out
y_pred = loaded_ann.predict(X)

print(y_pred)

#Execute server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)