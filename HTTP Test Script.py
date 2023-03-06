# Must run the following command to install requests:
# pip3 install requests
import requests

# This variable will count the total number of checks passed
counter = 0


def check_home_status(url):
    response = requests.get(url)
    return response.status_code


def deck_md5(url):
    response = requests.get(url)
    return response.status_code


def check_factorial_negative(url):
    response = requests.get(url)
    return response.status_code


# Must include the http://
# Example URL: http://127.0.0.1:8000/
api_url = input('Enter URL: ')

# ALL TESTS GO HERE
# TEST 1
response_code = check_home_status(api_url)
print(f"/ response code: {response_code}")

if response_code == 200:
    counter = counter + 1

# TEST 2
fact_neg = api_url + '/fibonacci/-1'
response_code = check_factorial_negative(fact_neg)
print(f"/ response code: {response_code}")

if response_code == 200:
    counter = counter + 1

print('{}/2 checks passed'.format(counter))
