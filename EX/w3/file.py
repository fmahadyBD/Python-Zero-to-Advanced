import os

f=open("x.txt","a")
f.write("This is tthe file python lectuer")
f.close()

f=open("x.txt","r")
print(f.read())
f.close()

if os.path.exists("x.txt"):
    os.remove("x.txt")
    print("File is removed")

else:
    print("This file is not exist")