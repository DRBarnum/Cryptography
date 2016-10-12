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
f=[]
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
            print(n) # Prints Message Numbers DELETE THIS
            a.append(n)
        key=input("Key: ")
        for c in key:
            m=(associations.find(c))
            print(m) # Prints Key Numbers DELETE THIS
            b.append(m)
        p=b*10
        for l in range(len(encryption)):
            q=a[l]+p[l]
            f.append(q)
        for h in f:
            k=associations[h]
            print(k, end="")
        print()
    elif start == "d":
        decryption=input("Message: ")
        key=input("Key: ")
    else:
        print("Did not understand command, try again.")



    
