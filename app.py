from flask import Flask, jsonify
from pymongo import MongoClient
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb+srv://imshu1:imshu1@cluster0.cagck.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") 
db = client.dashboard_db 
collection = db.insights 

@app.route('/load-data', methods=['GET'])
def load_data():
    try:
     
        with open('data/jsondata.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

     
        collection.insert_many(data)

        return jsonify({'message': 'Data loaded successfully!'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/data', methods=['GET'])
def get_data():
    try:
        data = list(collection.find({}, {"_id": 0}))  
        return jsonify(data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=4000)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)

