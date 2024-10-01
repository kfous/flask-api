from flask import Flask, request, jsonify
from transformers import pipeline
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv

import datetime
import os

app = Flask(__name__)

_ = load_dotenv(find_dotenv())  # read local .env file
# Connect to MongoDB
mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/sentiment_db')
client = MongoClient(mongo_uri)
db = client.sentiment_db
collection = db.sentiment_results  # The collection to store results

# Load the sentiment analysis model
sentiment_model = pipeline("sentiment-analysis")


@app.route('/predict', methods=['POST'])
def predict_sentiment():
    try:
        data = request.get_json()

        # Check if 'text' exists in the request data
        if not data or 'text' not in data:
            return jsonify({"error": "No text provided"}), 400

        text = data['text']

        # Get the sentiment analysis result (returns a list)
        result = sentiment_model(text)

        # Find the result with the highest score
        highest_score = max(result, key=lambda x: x['score'])

        # Return the label and score
        return jsonify({
            "label": highest_score['label'],
            "score": highest_score['score']
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    try:
        data = request.get_json()

        text = data['text']
        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Get the sentiment analysis result (returns a list)
        result = sentiment_model(text)

        # Find the result with the highest score
        highest_score = max(result, key=lambda x: x['score'])

        # Construct the document to be inserted into MongoDB
        document = {
            "text": text,
            "sentiment": highest_score['label'],
            "confidence_score": highest_score['score'],
            "timestamp": datetime.datetime.utcnow()  # Add timestamp for record tracking
        }

        # Insert the result into MongoDB
        collection.insert_one(document)

        # Return the label and score directly as JSON (no need for additional jsonify)
        return jsonify({
            "message": "Sentiment analysis completed and stored successfully.",
            "result": {
                "label": highest_score['label'],
                "score": highest_score['score']
            }
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
