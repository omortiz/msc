from flask import Flask, request, jsonify, render_template
import os
import requests
import json
import pusher
from src.sampleChat import SampleChatbot

app = Flask(__name__)

chatbot = SampleChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quest', methods = ['POST','GET'])
def quest():
    if request.method == 'POST':
        reponse = chatbot.get_response(request.form['message'])
        return json.dump({'reply':response})
    else:
        response = chatbot.get_response("Hi")
        return render_template('index.html', response=response)

# run Flask app
if __name__ == "__main__":
    app.run()
