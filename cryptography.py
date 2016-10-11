"""
cryptography.py
Author: Robbie
Credit: Mathew

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"


a=[]
b=[]
Coding=True
while Coding:
    start=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if start == "q":
        print("Goodbye")
        Coding=False
    elif start == "e":
        encryption=input("Mesage: ")
        for c in encryption:
            n=(associations.find(c))
            print(n)
            a.append(n)
        key=input("Key: ")
        for c in key:
            m=(associations.find(c))
            print(m)
            b.append(m)
        for l in range(len(encryption)):
            q=a[l]+b[l]
            print("Outcome", q)
    elif start == "d":
        decryption=input("Message: ")
        key=input("Key: ")
    else:
        print("Did not understand command, try again.")



    
