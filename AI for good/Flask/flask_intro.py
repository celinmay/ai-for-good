from flask import Flask, jsonify, request, render_template
import numpy as np
import pandas as pd
import csv 

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    symptoms = {'Fever': 0, 'Cough': 0, 'Problems Breathing': 0}
    return render_template("index.html", symptoms = symptoms)


@app.route("/data", methods=['POST', 'GET'])
def myFunction():
    if request.method == 'POST':
        symptomsList= request.form.getlist('symptom')
        for i in symptomsList:
            if i in symptomsList: 
                symptomsList[i] = 1
          

        fieldnames = ['symptom', 'symptom']   
        
        with open('data.csv', 'a') as inFile:  
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow({'symptom': symptomsList})
            return render_template("index.html")
 

#Execute server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)