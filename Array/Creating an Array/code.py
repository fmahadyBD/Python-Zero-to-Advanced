import array as arr

a=arr.array('i',[1,2,3,4])
# end means will print in the end not in next line
print("The new Created interger array: ",end="")
for i in range(0,3):
    print(a[i],end=" ")

print()
a=arr.array('d',[2.5,3.5,3.2,3.3])
print("The new Float Array: ",end=" ")
for i in range(0,3):
    print(a[i],end=" ")
