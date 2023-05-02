print("welcome to the g0-api service terminal")
print("for more information enter \"help\" or flag \"--help\" following a command")
print("\"exit\" to close terminal")


def help_text():
    print("this terminal allows one to interact with the remote api service")
    print("using this api entails one of four http methods, an endpoint, a payload, and a JSON response")
    print("the basic structure of commands is as follows:")
    print("[HTTP METHOD] /[ENDPOINT]/ ")
    print("allowed HTTP methods: GET, PUT, POST, DELETE")
    print("not all HTTP methods are allowed for every endpoint")
    print("endpoints: md5, factorial, fibonacci, is-prime, keyval")
    print("for more detailed instructions, enter a command followed by \"--help\"")
    print("\"exit\" to exit the terminal")


while True:
    terminal = input("$ ")
    match terminal:
        case "help":
            help_text()
        case "exit":
            exit()
