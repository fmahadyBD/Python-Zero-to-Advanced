import array as arr

#Appedn() function used in the code
#append only need the value not need the possition becouse it added the new item in end
# It only one value can added


a=arr.array('i',[1,2,3,4])
print("Before the append the array: ",end=" ")
for i in range(0,4):
    print(a[i],end=" ")
a.append(4)
print()

print("After the append.",end= " ")
for i in range(0,4):
    print(a[i],end=" ")


print()

# Extends() used for added multiple iltem .
# it added from the end of the privious array
    
b=arr.array('i',[1,2,3,4])
print("Before used extedns: ",end=" ")
for i in range(0,4):
    print(b[i],end=" ")

print()

c=arr.array('i',[5,6,7,8])
b.extend(c)
print("Used the  extends : ", end=" ")

for i in range(0,8):
    print(b[i],end=" ")


print()

# used insert
# insert function is most usefull to added value in positions

d=arr.array('i',[1,2,3,4])
print("Before use insert: ")
for i in range(0,4):
    print(d[i],end=" ")

print()

d.insert(1,0)
print("after used inster in  position 1")
for i in range(0,5):
    print(d[i],end=" ")



