import requests
import hashlib
import re
from distutils.util import strtobool
from getpass import getpass


def Main():
    loop = True
    print("Welcome to Password Checker")
    while loop:
        password = hashlib.sha1(
            getpass("Enter Password to test: ").encode()).hexdigest().upper()
        result = checkpassword(password)
        print(result)
        loop = strtobool(
            input("Do you wish to test another password? "
                  "[Yes, y] / [No, n] ").lower())


def checkpassword(password):
    # Take password input, hash, convert to text and make upper case
    front = password[:5]  # First 5 letters
    back = password[5:]  # rest of string

    # request the list of hashes
    pwlist = requests.get('https://api.pwnedpasswords.com/range/' + front)
    regex = r"{}:([0-9]*)".format(back)  # build regex
    result = re.search(regex, pwlist.text)

    if result is not None:  # If nothing found result is None
        return("Found your password {} times".format(
            result.group(1)))  # Group 1 for the number
    else:
        return("Your password was not found.")


if __name__ == "__main__":
    Main()
