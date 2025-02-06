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

## Amazon Prerequisites

### Configure Amazon CLI Credentials

1. **Install and configure Amazon CLI credentials:** Follow the instructions [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

2. **Create an Amazon S3 bucket** with a `GetObject` policy to access your files publicly. You can generate the policy [here](https://awspolicygen.s3.amazonaws.com/policygen.html).

### Create and Configure an Amazon EC2 Instance

1. **Connect to the instance** and run the following installations:

   ```bash
   sudo yum update -y
   sudo yum install -y git
   sudo yum install -y docker
   sudo service docker start
   sudo systemctl enable docker
   sudo usermod -a -G docker ec2-user
   exit
   sudo yum install python3-pip
   sudo pip3 install docker-compose
   ```

2. **Clone the repository:**

   ```bash
   git clone https://github.com/kfous/flask-api.git
   ```

3. **Navigate to the project directory** and create your `.env` file.

4. **Build and start the application:**

   ```bash
   docker-compose up --build -d
   ```

5. **Check running containers:**

   ```bash
   docker ps
   ```

---




