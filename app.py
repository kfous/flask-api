from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
