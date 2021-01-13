from flask import Flask, jsonify, request, render_template
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf 
import numpy as np
import pandas as pd
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
            # if you are looping through symptomsList, then every element here
            # will be in that list, the if condition isn't needed

            # however you need to be able to access the symptoms dictionary, James
            #sugested adding a function that wll return it, so added that at time commented out
            # and where you ould use it, line 23 and line 16 instead of line 17

            #if i in symptomsList: #not needed

            # here you want to edit the dictionary not symptomsList
            #symptoms[s] = 1 # if you used the canged loop
            symptoms[symptomsList[i]] = 1 # if you use range loop
            #    symptomsList[i] = int(symptomsList[1])


            fieldnames = ['symptom', 'symptom']

        with open('data.csv', 'a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=symptoms.keys())
            # here you need a loop to gothrough each element in dictionary
            # loop through symptoms.keys()
            
           # valueString = ''
            #for key, val in symptoms.items():
                    # write 0 to 1 to file
            #    writer.writerow(val)
                    # or if you need the values to be a single row then concatenate them to a string
               # valueString = valueString + format(val)
                # and write the 0 and 1 to to the file
               # writer.writerow(valueString)
           
            # symptomsList is a list, and cannot be appended like that I belive try the above method
            writer.writerow(symptoms)
            return render_template("index.html", symptoms = symptoms)

# Load model 
loaded_ann = keras.models.load_model('Covid_model')

# Trying it out
y_pred = loaded_ann.predict(X)

#Execute server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)