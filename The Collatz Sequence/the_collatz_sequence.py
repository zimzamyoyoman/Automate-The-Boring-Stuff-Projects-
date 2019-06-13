import sys

def collatz(number):
    if (number % 2 == 0):
        num=number//2
        print(num)
        return (num)
    else:
        num=number*3 + 1
        print(num)
        return(num)

print("Enter Number:")

try:
    number=input()
    number=int(number)
except: 
    print("Enter a valid number!")
    sys.exit()

while True:
    newNum=int(collatz(number))

    if (newNum!=1):
        number=newNum
        continue
    else:
        break

    