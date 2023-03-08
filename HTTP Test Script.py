# Must run the following command to install requests:
# pip3 install requests
import requests


def main():
    passed = 0
    tested = 0
    api_url = 'http://localhost:8000/'

    uri = ['', 'md5/', 'factorial/', 'fibonacci/', 'is-prime/']
    criteria = ['', '-1', '0', '1', '999', 'Howdy']

    for i in uri:
        for j in criteria:
            print(api_url + i + j)
            

    def http_status_check(url):
        response = requests.get(url)
        return response.status_code



    # ALL TESTS GO HERE
    # TEST 1
    response_code = check_home_status(api_url)
    print(f"/ response code: {response_code}")

    if response_code == 200:
        counter = counter + 1


    # Test checker
    print('{}/{} checks passed'.format(passed, tested))
    if passed == tested:
        return 0
    else:
        return 1


# Runs the script
main()
