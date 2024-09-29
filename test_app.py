import requests

if __name__ == '__main__':

    url = 'http://127.0.0.1:5000/predict'
    data = {'text': 'This is an amazing product!'}

    response = requests.post(url, json=data)

    # Print the raw response text
    print(response.text)

    # Optionally, check the status code
    print(f"Status Code: {response.status_code}")
