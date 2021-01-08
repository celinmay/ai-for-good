from flask import Flask, jsonify, request, render_template
import numpy as np
import pandas as pd
import csv 

app = Flask(__name__)
#Simple GET request to test app 

'''
@app.route("/")
def index():
  with open('symptom_frequency.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    first_line = True
    symptoms = []
    for row in data:
      if not first_line:
        symptoms.append({
          "symptom_1": row[0],
          "symptom_2": row[1],
          "symptom_3": row[2]
        })
      else:
        first_line = False
  return render_template("index.html", symptoms=symptoms)
'''

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/data', methods=["GET", "POST"])
def data_form():
    if request.method == "POST":
 
    checked=request.form['symptoms']
    with open('checked.txt', 'w') as file:
        file.write("%s"%checked)
    return checked

#Execute server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)