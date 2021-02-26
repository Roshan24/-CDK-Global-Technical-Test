from flask import Flask, request, url_for
import json
import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    newComment = {}
    with open('cases.json', 'r') as jFile:
        print(jFile)
        data = json.load(jFile)
        items = data[0]
        jFile.close()
    if request.method == 'POST':
        if request.form['comment'] != "" and request.form['comment'] != None:
            newComment['CommentBody'] = request.form['comment']
            newComment['CommentDate'] = datetime.datetime.now().isoformat()

            items['Comments'].append(newComment)
            data[0] = items

            with open('cases.json', 'w') as outfile:
                json.dump(data, outfile)
                outfile.close()
    return
