"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

start=input("Enter e to encrypt, d to decrypt, or q to quit: ")

if start == "e":
    m=input("Message: ")
elif start =="d":
    m=input("Mesage: ")
elif start=="q":
    print("Goodbye")
else:
    print("Did not understand command, try again.")