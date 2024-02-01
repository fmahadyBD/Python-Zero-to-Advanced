import array as arr
a=arr.array('i',[1,2,3,4,5])
print("Before use remove")
for i in range(0,5):
    print(a[i],end=" ")

print()
print("after use remove")

a.remove(1)
print("remove the item from the 1")
for i in range(0,4):
    print(a[i],end=" ")

print()
print("The pop function: ")

a.pop(1)
print("pop function work in position in 1:")
for i in range(0,3):
    print(a[i],end=" ")