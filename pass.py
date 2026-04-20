import string
import secrets

#   Variables
password = ""

#   List of characters
characters_list = string.ascii_letters + string.digits + string.punctuation

#   Generator loop
for _ in range(16):
    password += secrets.choice(characters_list)

#   Show generated password
print(password)