from flask import Flask, jsonify

app = Flask(__name__)
#Simple GET request to test app 

@app.route('/', methods=['GET'])
def home():
    return "Hello World"
    
#Execute server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)