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

while test == 0:
    command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    
    if command == "q":
        test = test + 1
        print("Goodbye!")
    elif command == "e":
        message = input("Message: ")
        key = input("Key: ")
    elif command == "d":
        pass
    else:
        print("Did not understand command, please try again.")
