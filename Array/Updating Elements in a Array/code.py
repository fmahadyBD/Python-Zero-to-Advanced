# this is replace mainly 
import array 
a=array.array('i',[1,2,3,4,5,6])
print("Before update:",end=" ")
for i in (a):
    print(i,end=" ")

print("\n After Update array: ")
a[2]=5

for i in (a):
    print(i,end=" ")