print("welcome to the g0-api service terminal")
print("for more information enter \"help\" or flag \"--help\" following a command")


def help_text():
    print("this terminal allows one to interact with the remote api service")
    print("using this api entails one of four http commands, an endpoint, a payload, and a JSON response")
    print("the structure of commands is as follows:")
    print

while True:
    terminal = input("$ ")
    match terminal:
        case "help":
            print("help selected")
