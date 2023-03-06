# Must run the following command to install requests:
# pip3 install requests
import requests

# This variable will count the total number of checks passed
counter = 0


def check_api_status(url):
    response = requests.get(url)
    return response.status_code


# Must include the http://
# Example URL: http://127.0.0.1:8000/
api_url = input('Enter URL: ')
response_code = check_api_status(api_url)
print(f"API response code: {response_code}")

if response_code == 200:
    counter = counter + 1