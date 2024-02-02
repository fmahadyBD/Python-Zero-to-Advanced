def tp(arr):
    n=len(arr)
    s=0 
    e=n-1
    flag=True
    temp=n*[None]
    for i in range(n):
        if flag is True:
            temp[i]=arr[e]
            e-=1
        else:
            temp[i]=arr[s]
            s+=1
        flag=bool(1-flag)
    
    
    for i in range(n):
        arr[i]=temp[i]
    
    print(arr)
    
    
l=[1,2,3,4,5,6,7]
tp(l)