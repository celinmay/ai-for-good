from flask import Flask, jsonify, request, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
#Simple GET request to test app 

import csv 

@app.route('/', methods=['GET'])
def home():
    return "Hello World"


    
#Execute server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)