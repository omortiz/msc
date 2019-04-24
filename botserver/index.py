from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import requests
import json
import pusher
from src.sampleChat import SampleChatbot

app = Flask(__name__)
CORS(app)

chatbot = SampleChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quest', methods = ['POST','GET'])
def quest():
    if request.method == 'POST':
        response = chatbot.get_response(request.form['message'])
        return json.dumps({'reply':str(response)})
    else:
        response = chatbot.get_response("Hi")
        return json.dumps({'reply':str(response)})

@app.route('/input', methods = ['POST','GET'])
def input():
    if request.method == 'POST':
        chatbot.train(request.form['input'])
        return json.dumps({'reply':True})
    else:
        response = chatbot.get_response("Hi")
        return json.dumps({'reply':False})

# run Flask app
if __name__ == "__main__":
    app.run()
