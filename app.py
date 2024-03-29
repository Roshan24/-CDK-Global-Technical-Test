from flask import Flask, render_template, request, url_for
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
            newComment['CreatedBy'] = items['Owner']['FirstName']+" "+items['Owner']['LastName']
            newComment['Id'] = "C-" + str(len(items['Comments'])+1)

            items['Comments'].append(newComment)
            items['LastModifiedDate'] = datetime.datetime.now().isoformat()

            data[0] = items

            with open('cases.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
                outfile.close()

    return render_template("home.html", items=items)


if __name__ == "__main__":
    app.run(debug=True)
