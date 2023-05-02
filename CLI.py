def main():
    while True:
        terminal = input("$ ").lower()

        if terminal == "help":
            help_text()
        if terminal == "exit":
            exit()

        inputs = terminal.split()

        url = 'http://34.16.146.25:80'
        methods = ["get", "put", "post", "delete"]
        endpoints = ["md5", "factorial", "fibonacci", "is-prime", "keyval"]

        if '--help' in inputs:
            contextual_help(inputs)

        print(f'unknown command: {terminal}')


print("welcome to the g0-api service terminal")
print("for more information enter \"help\" or flag \"--help\" following a command")
print("\"exit\" to close terminal")


def contextual_help(inputs):
    position = inputs.index('--help')
    print(position)
    if position == 0:
        method_help()

    elif position == 1:
        endpoint_help()

    elif position > 1:
        payload_help()

    else:
        print('unknown error with contextual_help')


def help_text():
    print("this terminal allows one to interact with the remote api service")
    print("using this api entails one of four http methods, an endpoint, a payload, and a JSON response")
    print("the basic structure of commands is as follows:")
    print("[HTTP METHOD] [ENDPOINT] [ARGUMENTS]")
    print("allowed HTTP methods: GET, PUT, POST, DELETE")
    print("not all HTTP methods are allowed for every endpoint")
    print("endpoints: md5, factorial, fibonacci, is-prime, keyval")
    print("for more detailed instructions, enter a command followed by \"--help\"")
    print("\"exit\" to exit the terminal")


def method_help(method):
    print("different http methods do different things to each endpoint")
    print("not every method is allowed for every endpoint, a 405 error will be raised if it is not")
    print("contextual help for the method you specified:")

    if method == 'get':
        print("The get method is allowed for all endpoints")
        print("for specific usage, type \"get [endpoint] --help\"")
    elif method == 'put':
        print("The put method is only allowed for /keyval/")
        print("for specific usage, type \"put keyval --help\"")
    elif method == 'post':
        print("The post method is only allowed for /keyval/")
        print("for specific usage, type \"post keyval --help\"")
    elif method == 'delete':
        print("The delete method is only allowed for /keyval/")
        print("for specific usage, type \"delete keyval --help\"")


def endpoint_help(endpoint):
    print('endpoint help')


def payload_help():
    print('payload help')

main()
