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
    # emoji = {0: '✓ | button | check | mark', 1: '× | cancel | cross | mark | multiplication | multiply | x'}

    for i in uri:
        for j in criteria:
            current_uri = api_url + i + j
            response_code = http_status_check(current_uri)

            if response_code == expected[position]:
                passed = passed + 1
                emoji = u'\u2705'
            else:
                emoji = u'\u274C'
            tested = tested + 1
            position = position + 1

            str_code = str(response_code)
            print(f"{current_uri:<40}{'Response code: ':>20}{response_code}{emoji:>5}")

    # Test checker
    print()
    print('{}/{} checks passed'.format(passed, tested))
    if passed == tested:
        print('Finished with code 0')
        return 0
    else:
        print('Finished with code 1')
        return 1


# Runs the script
main()
