# Must run the following command to install requests:
# pip3 install requests
import requests


def main():
    # This variable will count the total number of checks passed
    counter = 0

    def check_home_status(url):
        response = requests.get(url)
        return response.status_code

    def check_md5(url):
        response = requests.get(url)
        return response.status_code

    def check_factorial_negative(url):
        response = requests.get(url)
        return response.status_code

    api_url = 'http://localhost:8000/'

    # ALL TESTS GO HERE
    # TEST 1
    response_code = check_home_status(api_url)
    print(f"/ response code: {response_code}")

    if response_code == 200:
        counter = counter + 1

    # TEST 2
    md5 = api_url + '/md5/'
    response_code = check_md5(md5)
    print(f"/md5/ response code: {response_code}")

    if response_code == 200:
        counter = counter + 1

    # TEST 3
    md5_0 = api_url + '/md5/0'
    response_code = check_md5(md5_0)
    print(f"/md5/0 response code: {response_code}")

    if response_code == 200:
        counter = counter + 1

    # TEST 4
    fact_neg = api_url + '/factorial/-1'
    response_code = check_factorial_negative(fact_neg)
    print(f"/factorial/-1 response code: {response_code}")

    if response_code == 200:
        counter = counter + 1

    # TEST 5
    fact_0 = api_url + '/factorial/0'
    response_code = check_factorial_negative(fact_0)
    print(f"/factorial/0 response code: {response_code}")

    if response_code == 200:
        counter = counter + 1

    # TEST 6
    fact_1 = api_url + '/factorial/1'
    response_code = check_factorial_negative(fact_1)
    print(f"/factorial/1 response code: {response_code}")

    if response_code == 200:
        counter = counter + 1

    # TEST 7
    fact_999 = api_url + '/factorial/999'
    response_code = check_factorial_negative(fact_999)
    print(f"/factorial/999 response code: {response_code}")

    if response_code == 200:
        counter = counter + 1

    # Test checker
    print('{}/7 checks passed'.format(counter))
    total_tests = 6
    if counter == total_tests:
        return 0
    else:
        return 1


# Runs the script
main()
