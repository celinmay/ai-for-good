from flask import Flask, jsonify, request, render_template
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf 
import numpy as np
from keras.models import load_model
import pandas as pd
import csv


app = Flask(__name__)


def fetchSymptoms():
    return {'Breathing Problem':0,	'Fever':0,	'Dry Cough':0,	'Sore throat':0, 'Running Nose':0, 'Asthma':0, 'Chronic Lung Disease':0, 'Headache':0, 'Heart Disease':0, 'Diabetes':0, 'Hyper Tension':0, 'Fatigue':0,	'Gastrointestinal':0, 'Abroad travel':0, 'Contact with COVID Patient':0, 'Attended Large Gathering':0, 'Visited Public Exposed Places':0, 'Family working in Public Exposed Places':0, 'Wearing Masks':0, 'Sanitization from Market':0}



@app.route("/", methods=['GET'])
def index():
    symptoms = fetchSymptoms()
    return render_template("CM_CovidMeter.html", symptoms = symptoms)


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
            writer = csv.DictWriter(inFile, fieldnames=symptoms.keys(), lineterminator = '\n')
           # writer = csv.writer(inFile)

            writer.writerow(symptoms)
            return render_template("CM_CovidMeter.html", symptoms = symptoms)

@app.route("/results", methods=['GET'])
def results():
   # X

    dataset = pd.read_csv('data.csv') # Enter dataset
    X = dataset.iloc[-1,:]
    X = np.array([X], dtype = np.float64)
    X = np.reshape(X, (-1,20))

# Load model 
    loaded_ann = keras.models.load_model('Covid_model')

#Trying it out
    y_pred = loaded_ann.predict(X)

    print(y_pred)
  
    return str(y_pred[0])



#Execute server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
