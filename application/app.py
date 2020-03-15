from flask import Flask, escape, request,render_template
from pymongo import MongoClient

app = Flask(__name__)
MONGO_URI = 'mongodb://localhost'
client = MongoClient(MONGO_URI)

db = client['NodeCar']
collection = db['data']

collection.insert_one({"Type":"Tesla Killer 111"})

@app.route('/')
def hello():
    result = collection.find()
    # app = Flask(__name__)
    obj = {}
    for r in result:
        obj['Type'] = r['Type']

    return render_template('index.html',obj=obj)

if __name__=="__main__":
    app.run(port = 3006, debug = True)