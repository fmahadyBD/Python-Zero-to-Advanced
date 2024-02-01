import array as arr
# use indext to find the 
a=arr.array("i",[1,2,3,1,2,5])
print("The array")
for i in (a):
    print(i,end=" ")

print("\nThe 1st occutrence 2's index is :",end=" ")
print(a.index(2))
print("The 1st occurrence of 1's index: ",end=" ")
print(a.index(1))