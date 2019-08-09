#! python3
# strongPasswordDetector.py - Detects whether a password is strong enough

import re

print("Enter a strong password!")
password = input()

passwordLengthRegex = re.compile(r'.{8,}')
passwordMatch = passwordLengthRegex.search(password)

if (passwordMatch):
    passwordUpperCaseRegex = re.compile(r'[A-Z]+')
    passwordMatch = passwordUpperCaseRegex.search(password)

    if (passwordMatch):
        passwordLowerCaseRegex = re.compile(r'[a-z]+')
        passwordMatch = passwordLowerCaseRegex.search(password)

        if (passwordMatch):
            passwordNumberRegex = re.compile(r'[0-9]+')
            passwordMatch = passwordNumberRegex.search(password)

            if (passwordMatch):
                print("Password is STRONG.")

            else:
                print("Password must contain atleast one digit.")


        else:
            print("Password must contain atleast one lowercase character.") 

    else:
        print("Password must contain atleast one uppercase character.")
else:
    print("Password must be longer than 8 characters.")
