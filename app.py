import os
from flask import Flask, json, jsonify
from pymongo import MongoClient
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Set up MongoDB connection
client = MongoClient("mongodb+srv://imshu1:imshu1@cluster0.cagck.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.dashboard_db  # Database
collection = db.insights  # Collection

@app.route('/load-data',methods=['GET'])
def load_data():
    try:
        # Load JSON file
        with open('data/jsondata.json', 'r') as file:
            data = json.load(file)

        # Insert data into MongoDB collection
        collection.insert_many(data)

        return jsonify({'message': 'Data loaded successfully!'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API route to get all data
@app.route('/api/data', methods=['GET'])
def get_all_data():
    try:
        # Fetch all data from MongoDB
        data = list(collection.find({}, {"_id": 0}))  # Avoid returning MongoDB _id field
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))  # Default to 5000 if PORT isn't set
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)

