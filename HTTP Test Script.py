# Must run the following command to install requests:
# pip3 install requests
import requests


def check_api_status(url):
    response = requests.get(url)
    return response.status_code


# Example usage
api_url = input('Enter URL')
response_code = check_api_status(api_url)
print(f"API response code: {response_code}")
