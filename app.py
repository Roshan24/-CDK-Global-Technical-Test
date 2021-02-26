from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def home():
    newComment = {}
    with open('cases.json', 'r') as jFile:
        print(jFile)
        data = json.load(jFile)
        jFile.close()
