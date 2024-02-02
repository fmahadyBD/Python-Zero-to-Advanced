def zeromove(arr):
    c=0
    n=len(arr)
    for i in range(0,len(arr)):
        if arr[i]!=0:
         arr[c]=arr[i]
         c+=1
    while c<n:
        arr[c]=0 
        c+=1  
    print(arr)
    
v=[1,2,0,0,0,1,2,4,0,7]
zeromove(v)