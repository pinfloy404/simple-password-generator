import argparse
import sys
import string
import secrets

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
    print(f"{password}")

#   Run main fuction
if __name__ == "__main__":
    main()