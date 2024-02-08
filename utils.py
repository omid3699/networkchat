import sys
from time import sleep

from colorama import Fore, Style
from pickle import loads, dumps

def sprint(username, msg):
    print(Style.BRIGHT + Fore.BLUE + username + Style.RESET_ALL + Fore.RED, end=": ")
    for i in msg:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.1)
    sys.stdout.write("\n" + Fore.RESET)
    sys.stdout.flush()


def validate_username(username):
    if not username:
        return False
    username = username.replace(" ", "")
    invalid_chars = [
        "~",
        "`",
        "@",
        "!",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        "_",
        "-",
        "[",
        "]",
    ]
    for i in username:
        if i in invalid_chars:
            return False
    return username.title()

def encode(data):
    return dumps(data)

def decode(data):
    return loads(data)

