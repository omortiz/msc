from flask import Flask, request, jsonify, render_template
import os
import dialogflow
import requests
import json
import pusher
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    text_content = random.choice(["hello Abril!", "I am happy!", "Nice to meet you"])
    response_text = { "message":  text_content }
    return jsonify(response_text)

# run Flask app
if __name__ == "__main__":
    app.run()
