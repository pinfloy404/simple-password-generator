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

#   Character list length constant
CH_LIST_LENGTH = 4

#   Character list total length
CH_TOTAL_LENGTH = len(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)

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

#   Function to add the extra numbers of mod operation to the characters dict
def extra_selection(args: argparse.Namespace, characters_dict: dict[str, int]):
    #   Get the extra numbers of mod operation
    extra = int(args.length % CH_LIST_LENGTH)

    #   Dictionary to list
    characters_list = list(characters_dict)

    #   Random sum of extra numbers for character type selection
    while extra > 0:
        #   Create a number range inside extra variable range (1 -> extra)
        extra_range = (secrets.randbelow(extra) + 1)

        #   Get random index from dictionary
        index = secrets.randbelow(len(characters_list))

        #   Get key
        key = characters_list[index]

        #   Change key's value by adding the number range
        value = (characters_dict.get(key) + extra_range)

        #   Adding key's modified value
        characters_dict[key] = value

        #   Removing the range used
        extra -= extra_range

#   Function to password generation
def password_generator(args: argparse.Namespace, characters_dict: dict[str, int]) -> str:
    #   Password string
    password = ""

    #   Dictionary to list
    characters_list = list(characters_dict)

    #   Generator loop
    for _ in range(args.length):
        #   Get random index from dictionary
        index = secrets.randbelow(len(characters_list))

        #   Get key
        key = characters_list[index]

        #   Change key's value by reducing the number range
        value = (characters_dict.get(key) - 1)

        #   Adding key's modified value
        characters_dict[key] = value

        #   Get random character
        character = secrets.choice(characters_list[index])

        #   Adding a character to password string
        password += character

        #   If password length is less than 94 (all ascii strings combined), then it can have unique letters
        if args.length <= CH_TOTAL_LENGTH:
            characters_list[index].replace(character, '')

        #   If selection number is 0, the selected string isn't in use anymore
        if value == 0:
            characters_list.remove(key)

    #   Return password generated
    return password

#   Prints password in terminal
def print_password(args: argparse.Namespace, password: str):
    #   If color argument is False, prints the password and exits correctly
    if args.color is False:
        print(password) 
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

    #   Show the colored password
    print(colored_password)

#   Main function
def main():
    #   Get arguments
    args = get_args()

    #   Minimum length check
    if args.length < 12:
        print(f'arg error: length -> {args.length} < 12')

        #   Script exit
        sys.exit(1)

    #   Divide the password length into character list length and saves the extra from mod
    selection = int(args.length / CH_LIST_LENGTH)

    #   Dictionary of characters
    characters_dict = {string.ascii_lowercase : selection, string.ascii_uppercase : selection, string.digits : selection, string.punctuation : selection}

    #   Calls extra numbers function
    extra_selection(args, characters_dict)

    #   Calls password generator
    password = password_generator(args, characters_dict)

    #   Show generated password
    print_password(args, password)

#   Run main fuction
if __name__ == "__main__":
    main()