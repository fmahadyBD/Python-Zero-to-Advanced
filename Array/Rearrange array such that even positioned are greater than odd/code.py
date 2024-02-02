def roe(arr):
    n=len(arr)
    x=1
    for i in range(0,n-1,2):
        if arr[i] > arr[x]:
            arr[i],arr[x]=arr[x],arr[i]
        x+=2
        
    print(arr)
    
v=[1,3,2,1,2,3,4,5,6]
roe(v)