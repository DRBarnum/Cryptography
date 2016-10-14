"""
cryptography.py
Author: Robbie
Credit: Mathew

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"



Coding=True
while Coding:
    start=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if start = "q":
        print("Goodbye")
        Coding=False
    elif start == "e":
        a=[]
        b=[]
        f=[]
        encryption=input("Mesage: ")
        for c in encryption:
            n=(associations.find(c))
            a.append(n)
        key=input("Key: ")
        for c in key:
            m=(associations.find(c))
            b.append(m)
        p=b*10 
        for l in range(len(encryption)):
            q=a[l]+p[l]
            if q >= 84:
                j=q-84
                f.append(j)
            else:
                f.append(q)
        for h in f:
            k=associations[h]
            print(k, end="")
        print()
    elif start == "d":
        z=[]
        w=[]
        u=[]
        decryption=input("Message: ")
        for c in decryption:
            n=(associations.find(c))
            w.append(n)
        key=input("Key: ")
        for c in key:
            m=(associations.find(c))
            z.append(m)
        p=z*10 
        for l in range(len(decryption)):
            q=w[l]-p[l]
            if q <= 0:
                j=q+84
                u.append(j)
            else:
                u.append(q)
        for h in u:
            k=associations[h]
            print(k, end="")
        print()
    else:
        print("Did not understand command, try again.")



    
