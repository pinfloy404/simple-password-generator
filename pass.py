import argparse
import string
import secrets

#   Argument parser function
def get_args():
    #   Create parser object
    parser = argparse.ArgumentParser(prog='Simple Password Generator', description='A simple password generator in Python.')
    
    #   Length argument
    parser.add_argument('-l', '--length', type=int, default=16, help='Password length. By default it\'s 16 characters')

    #   Returns parsed arguments
    return parser.parse_args()

#   Main function
def main():
    #   Variables
    args = get_args()
    password = ""

    #   List of characters
    characters_list = string.ascii_letters + string.digits + string.punctuation

    #   Generator loop
    for _ in range(args.length):
        password += secrets.choice(characters_list)

    #   Show generated password
    print(password)

#   Run main fuction
if __name__ == "__main__":
    main()