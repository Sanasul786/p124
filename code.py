from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
    {
        'id':1,
        'Name':u'Raju',
        'Contact':u'897564379',
        'done':False
    },
    {
        'id':2,
        'Name':u'Rahul',
        'Contact':u'1109835622',
        'done':False
    }
]
@app.route("/")
def hello_world():
    return "Hello world"
@app.route("/add-data",methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
        contact = {
            'id':tasks[-1]['id']+1,
            'Name':request.json['Name'],
            'Contact':request.json.get('Contact',""),
            'done':False
        }
        lists.append(contact)
        return jsonify({
            "status":"Success",
            "message":"contact added successfully"
        })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":lists,
    })
if (__name__ == "__main__"):
    app.run()
