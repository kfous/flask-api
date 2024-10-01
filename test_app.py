import requests


def test_predict():
    url = 'http://127.0.0.1:5000/predict'
    data = {'text': 'This is an amazing product!'}

    response = requests.post(url, json=data)

    # Print the raw response text
    print(response.text)

    # Optionally, check the status code
    print(f"Status Code: {response.status_code}")

def test_analyze():
    url = 'http://127.0.0.1:5000/analyze'
    data = {'text': 'This is an crappy product.'}

    response = requests.post(url, json=data)

    # Print the raw response text
    print(response.text)

    # Optionally, check the status code
    print(f"Status Code: {response.status_code}")


if __name__ == '__main__':
    print("Test of /predict: ")
    test_predict()
    print("Test of /analyze: ")
    test_analyze()
