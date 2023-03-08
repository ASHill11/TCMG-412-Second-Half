# Must run the following command to install requests:
# pip3 install requests
import requests


def main():

    def http_status_check(url):
        response = requests.get(url)
        return response.status_code

    passed = 0
    tested = 0
    api_url = 'http://localhost:8000/'

    uri = ['', 'md5/', 'factorial/', 'fibonacci/', 'is-prime/']
    criteria = ['', '-1', '0', '1', '999', 'Howdy']
    expected = [200, 404, 404, 404, 404, 404, 200, 200, 200, 200, 200, 200, 200, 404, 200, 200, 200, 404, 200, 404, 200,
                200, 200, 404, 200, 404, 200, 200, 200, 404]
    position = 0

    for i in uri:
        for j in criteria:
            current_uri = api_url + i + j
            response_code = http_status_check(current_uri)

            str_code = str(response_code)
            print(f"{current_uri:<37}{response_code:>10}")

            if response_code == expected[position]:
                passed = passed + 1
            tested = tested + 1
            position = position + 1


    # Test checker
    print()
    print('{}/{} checks passed'.format(passed, tested))
    if passed == tested:
        return 0
    else:
        return 1


# Runs the script
main()
