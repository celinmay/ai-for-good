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
def data():
    if request.method == 'POST':
        file = request.form['symptom1']
        data = pd.read_excel(file)
        return render_template('data.html', data=data.to_html())
    
    
#Execute server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)