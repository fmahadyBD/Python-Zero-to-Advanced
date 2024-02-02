def z(arr):
    n=len(arr)
    j=0
    for i in range(n):
        if arr[i]!=0:
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
            
    print(arr)
    
v=[1,2,0,9,0,9,0,4,0,7]
z(v)