from flask import Flask,jsonify,request

app = Flask(__name__)

contacts = [
    {
        'Contact': "1234567890",
        'Name' : "Ralph",
        'done' : False,
        "id" : 1
    },
    {
        'Contact': "0987654321",
        'Name' : "Alph",
        'done' : False,
        "id" : 2
    }
]

@app.route("/add-data",methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            'status' : "error",
            'message' : "pls provide the data"
        }, 400)

    contact = {
        'id' : contacts[-1]['id']+1,
        'Name' : request.json['Name'],
        'Contact' : request.json.get('Contact',""),
        'done' : False
    }

    contacts.append(contact)

    return jsonify({
        "status":"success",
        "message":"contact added successfuly" 
    },400)
