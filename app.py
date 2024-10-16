import requests
import datetime
import os
import boto3

from flask import Flask, request, jsonify
from transformers import pipeline
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv


app = Flask(__name__)

_ = load_dotenv(find_dotenv())  # read local .env file
# Connect to MongoDB
mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/sentiment_db')
client = MongoClient(mongo_uri)
db = client.sentiment_db
# The collection to store results
collection = db.sentiment_results

# Load the sentiment analysis model
sentiment_model = pipeline("sentiment-analysis")

# AWS S3 Configuration
s3_client = boto3.client('s3')
BUCKET_NAME = os.getenv('BUCKET_NAME')


@app.route('/sentiment', methods=['POST'])
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


@app.route('/save', methods=['POST'])
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


# Useful to check if you can access your files via presigned url
@app.route('/generate-url', methods=['POST'])
def generate_presigned_url():
    data = request.json

    # Check if the request contains the 'file_key'
    if not data or 'file_key' not in data:
        return jsonify({"error": "file_key is required"}), 400

    file_key = data['file_key']

    try:
        # Generate the pre-signed URL
        presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': BUCKET_NAME, 'Key': file_key},
            ExpiresIn=3600  # URL expiration time in seconds (1 hour)
        )
        return jsonify({"presigned_url": presigned_url}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Use the presigned url text file contents to do sentiment analysis on IMDB Review
@app.route('/sentiment-url', methods=['POST'])
def sentiment_url():
    data = request.json

    # Check if the request contains the 'file_key'
    if not data or 'presigned_url' not in data:
        return jsonify({"error": "presigned_url is required"}), 400

    presigned_url = data['presigned_url']

    try:
        response = requests.get(presigned_url)
        text = response.text
        # Roberta model has a max length of 512 tokens. Let's check sentiment until then.
        truncated_text = text[:512]

        # Get the sentiment analysis result (returns a list)
        result = sentiment_model(truncated_text)

        # Find the result with the highest score
        highest_score = max(result, key=lambda x: x['score'])

        # Return the label and score
        return jsonify({
            "label": highest_score['label'],
            "score": highest_score['score']
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/sent-url-save', methods=['POST'])
def sentiment_url_save():
    data = request.json

    # Check if the request contains the 'file_key'
    if not data or 'presigned_url' not in data:
        return jsonify({"error": "presigned_url is required"}), 400

    presigned_url = data['presigned_url']

    try:
        response = requests.get(presigned_url)
        text = response.text
        # Roberta model has a max length of 512 tokens. Let's check sentiment until then.
        truncated_text = text[:512]

        # Get the sentiment analysis result (returns a list)
        result = sentiment_model(truncated_text)

        # Find the result with the highest score
        highest_score = max(result, key=lambda x: x['score'])

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
            "message": "Sentiment analysis for IMDB Review completed and stored successfully.",
            "result": {
                "label": highest_score['label'],
                "score": highest_score['score']
            }
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
