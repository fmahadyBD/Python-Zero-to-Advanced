x=5
y=9
print(x+y)

print(x)
print(y)
z=float(x)
zz=str(x)
print(z)
print(zz)
print(type(x))
print(type(zz))


# Mutipale value
x,y,z="Mahady ","Hasan","Fahim"
print(x)
print(y)
print(z)

x=y=z="Fahiim"
print(x)

# Unpack acollection
nams=["Mahady","Hasan","Fahim"]
x,y,z=nams
print(x)
print(y)
print(z)
print(x,y,z)
print(x+y+z)



# Global Function

x="awesome"
def mufun():
    print("this is the "+x)

mufun()

x="Fine"

def myfun():
    print(x)

myfun()
print("1"+x)


# Use Global

def my():
    global x
    x="Fahim"
my()

print(x)