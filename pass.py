import argparse
import sys
import string
import secrets

#   Colors
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

#   Argument parser function
def get_args():
    #   Create parser object
    parser = argparse.ArgumentParser(prog='Simple Password Generator', description='A simple password generator in Python.')
    
    #   Length argument
    parser.add_argument('-l', '--length', type=int, default=16, help='Password length. By default it\'s 16 characters. Minimum of 12 characters')

    #   Color argument
    parser.add_argument('-c', '--color', action='store_true', help='Enables color differentiation by character type')

    #   Returns parsed arguments
    return parser.parse_args()

#   Function to password generation
def password_generator(args: argparse.Namespace, characters_list: list[str]) -> str:
    #   Password string
    password = ""

    #   Generator loop
    for _ in range(args.length):
        #   Get random index from dictionary
        index = secrets.randbelow(len(characters_list))

        #   Adding a random character to password string
        password += secrets.choice(characters_list[index])

    #   Returns password generated
    return password

#   Prints password in terminal
def print_password(args: argparse.Namespace, password: str):
    #   If color argument is False, prints the password and exits correctly
    if args.color is False:
        #   Shows uncolored  password
        print(password)

        #   Script exit correctly
        sys.exit(0)

    #   Colored password string
    colored_password = ""

    #   Coloring loop, if the character is in some of these character lists, then it colours with a color
    for character in password:
        #   Lowercase letters in blue
        if character in string.ascii_lowercase:
            colored_password += f"{BLUE}{character}{RESET}"
            continue

        #   Uppercase letters in green
        if character in string.ascii_uppercase:
            colored_password += f"{GREEN}{character}{RESET}"
            continue

        #   Digits in red
        if character in string.digits:
            colored_password += f"{RED}{character}{RESET}"
            continue

        #   Special characters in yellow
        if character in string.punctuation:
            colored_password += f"{YELLOW}{character}{RESET}"
            continue

    #   Shows the colored password
    print(colored_password)

#   Main function
def main():
    #   Gets arguments
    args = get_args()

    #   Minimum length check
    if args.length < 12:
        print(f'arg error: length -> {args.length} < 12')

        #   Script exit with error
        sys.exit(1)

    #   List of characters
    characters_list = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]

    #   Calls password generator function
    password = password_generator(args, characters_list)

    #   Calls password coloring function
    print_password(args, password)

#   Run main fuction
if __name__ == "__main__":
    main()