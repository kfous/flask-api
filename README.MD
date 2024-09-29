# REST API Application with Flask

This is a REST API application built using Flask. It leverages a pre-trained sentiment analysis model to execute and generate a list of sentiment results.

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
    docker-compose build

2. Start the application
    ```bash
    docker-compose up
3. (Optional) Run the test file to test a POST request:
    ```bash
    python test_app.py
