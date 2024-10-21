import requests


def test_sentiment():
    url = 'http://127.0.0.1:5000/sentiment'
    data = {'text': 'This is an amazing product!'}

    response = requests.post(url, json=data)

    # Print the raw response text
    print(response.text)

    # Optionally, check the status code
    print(f"Status Code: {response.status_code}")


def test_save():
    url = 'http://127.0.0.1:5000/save'
    data = {'text': 'This is an crappy product.'}

    response = requests.post(url, json=data)

    # Print the raw response text
    print(response.text)

    # Optionally, check the status code
    print(f"Status Code: {response.status_code}")


def test_gen_presigned_url():
    url = 'http://127.0.0.1:5000/generate-url'
    data = {'file_key': 'sentiment_txts/review1.txt'}

    response = requests.post(url, json=data)

    # Print the raw response text
    print(response.text)

    # Optionally, check the status code
    print(f"Status Code: {response.status_code}")


def test_sentiment_url():
    url = 'http://127.0.0.1:5000/sentiment-url'
    data = {
        'presigned_url': 'add-your-url-here'}

    response = requests.post(url, json=data)

    # Print the raw response text
    print(response.text)

    # Optionally, check the status code
    print(f"Status Code: {response.status_code}")


def test_sentiment_url_save():
    url = 'http://127.0.0.1:5000/sent-url-save'
    data = {
        'presigned_url': 'add-your-url-here'}

    response = requests.post(url, json=data)

    # Print the raw response text
    print(response.text)

    # Optionally, check the status code
    print(f"Status Code: {response.status_code}")


def run_tests():
    print("Choose a test to run (1-5):")
    print("1. Test of /sentiment")
    print("2. Test of /save")
    print("3. Test of /gen-url")
    print("4. Test of /sentiment-url")
    print("5. Test of /sentiment-url-save")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("Test of /sentiment: ")
        test_sentiment()
    elif choice == "2":
        print("Test of /save: ")
        test_save()
    elif choice == "3":
        print("Test of /gen-url: ")
        test_gen_presigned_url()
    elif choice == "4":
        print("Test of /sentiment-url: ")
        test_sentiment_url()
    elif choice == "5":
        print("Test of /sentiment-url-save: ")
        test_sentiment_url_save()
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == '__main__':
    run_tests()
