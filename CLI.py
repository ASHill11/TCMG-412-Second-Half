print("welcome to the g0-api service terminal")
print("for more information enter \"help\" or flag \"--help\" following a command")
print("\"exit\" to close terminal")


def help_text():
    print("this terminal allows one to interact with the remote api service")
    print("using this api entails one of four http methods, an endpoint, a payload, and a JSON response")
    print("the structure of commands is as follows:")
    print("[HTTP METHOD] /[ENDPOINT] ")


while True:
    terminal = input("$ ")
    match terminal:
        case "help":
            print("help selected")
        case "exit":
            exit()
