#! python3
# regexStrip.py - A form of the strip() function using regular expressions

import re

def regexStrip(string, character):


    if not character:
        blankRegex = re.compile(r'^[\s]*')
        result=blankRegex.sub('', string)
        blankRegex = re.compile(r'[\s$]*')
        result=blankRegex.sub('', result)
        return result
        
    else:
        characterRegex = re.compile(r'^(%s)*'%character)
        result=characterRegex.sub('',string)
        characterRegex = re.compile(r'(%s$)*'%character)
        result=characterRegex.sub('',result)
        return result

print("Enter the string to be stripped")
string=input()
print("Enter the character to remove")
character=input()
result=regexStrip(string,character)
print(result)

