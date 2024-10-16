# REST API Application with Flask

This is a REST API application built using Flask. It leverages a pre-trained sentiment analysis model to execute and generate a list of sentiment results.
The input for the sentiment analysis comes from 20 IMDB movie reviews.\
The reviews are retrieved from text files located in an AWS S3 Instance.

## Installation

To set up the application, you can choose one of the following methods:

### Method 1: Using Python

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
2. Run the application:
    ```bash
    python app.py
3. (Optional) Run the test file to test a POST request:
    ```bash
    python test_app.py

### Method 2: Using Docker
1. Build application with Docker
    ```bash
    docker compose build

2. Start the application
    ```bash
    docker compose up
3. (Optional) Run the test file to test the POST requests:
    ```bash
    python test_app.py

## Check results
Download Studio 3T: [here](https://studio3t.com) and connect to MongoDB:
- Make a local Mongodb connection using the mongo URI: mongodb://localhost:27017/sentiment_db
- If POST requests were successful, sentiment is stored in sentiment_db/sentiment_results.

## Amazon Prerequisites:
1. Configure Amazon CLI credentials: [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
2. Create an Amazon S3 bucket with a GetObject policy in order to access your files publicly: [here](https://awspolicygen.s3.amazonaws.com/policygen.html)