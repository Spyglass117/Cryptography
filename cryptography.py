"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
test = 0
str1 = ""
str2 = ""

while test == 0:
    command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    n = 0
    if command == "q":
        test = test + 1
        print("Goodbye!")
    elif command == "e":
        message = input("Message: ")
        key = input("Key: ")
        while len(key) < len(message):
            key += key
        associations += associations
        l = len(message)
        while n < l:
            numrepm = associations.find(message[n])
            numrepk = associations.find(key[n])
            finalnum = numrepm + numrepk
            letrep = associations[finalnum]
            str1 = str1 + letrep
            n = n + 1
        print(str1)
    elif command == "d":
        message = input("Message: ")
        key = input("Key: ")
        while len(key) < len(message):
            key += key
        associations += associations
        l = len(message)
        while n < l:
            numrepm1 = associations.find(message[n])
            numrepk1 = associations.find(key[n])
            finalnum1 = numrepm1 - numrepk1
            letrep1 = associations[finalnum1]
            str2 = str2 + letrep1
            n = n + 1
        print(str2)
    else:
        print("Did not understand command, try again.")
