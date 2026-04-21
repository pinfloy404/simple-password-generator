import argparse
import sys
import string
import secrets

#   Argument parser function
def get_args():
    #   Create parser object
    parser = argparse.ArgumentParser(prog='Simple Password Generator', description='A simple password generator in Python.')
    
    #   Length argument
    parser.add_argument('-l', '--length', type=int, default=16, help='Password length. By default it\'s 16 characters. Minimum of 12 characters')

    #   Returns parsed arguments
    return parser.parse_args()

#   Main function
def main():
    #   Get arguments
    args = get_args()

    #   Password string
    password = ""

    #   Character list length constant
    CH_LIST_LENGTH = 4

    #   Divide the password length into character list length and saves the extra from mod
    selection = int(args.length / CH_LIST_LENGTH)
    extra = int(args.length % CH_LIST_LENGTH)

    #   Minimum length check
    if args.length < 12:
        print(f'arg error: length -> {args.length} < 12')

        #   Script exit
        sys.exit(1)

    #   Dictionary of characters
    characters_list = {string.ascii_lowercase : selection, string.ascii_uppercase : selection, string.digits : selection, string.punctuation : selection}

    #   Random sum of extra numbers for character type selection
    while extra > 0:
        #   Create a number range inside extra variable range (1 -> extra)
        extra_range = (secrets.randbelow(extra) + 1)

        #   Get random index from dictionary
        index = secrets.randbelow(len(characters_list))

        #   Get key
        key = list(characters_list)[index]

        #   Change key's value by adding the number range
        value = (characters_list.get(key) + extra_range)

        #   Adding key's modified value
        characters_list[key] = value

        #   Removing the range used
        extra -= extra_range

    #   Generator loop
    for _ in range(args.length):
        #   Get random index from dictionary
        index = secrets.randbelow(len(characters_list))

        #   Get key
        key = list(characters_list)[index]

        #   Change key's value by adding the number range
        value = (characters_list.get(key) - 1)

        #   Adding key's modified value
        characters_list[key] = value

        #   Adding a character to password string
        password += secrets.choice(list(characters_list)[index])

        #   If selection number is 0, the selected string isn't in use anymore
        if value == 0:
            characters_list.pop(key)

    #   Show generated password
    print(f"{password}")

#   Run main fuction
if __name__ == "__main__":
    main()