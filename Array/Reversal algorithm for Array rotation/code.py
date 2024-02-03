def rever(arr,start,end):
    while start<end:
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end-=1

def raar(arr,d):
    rever(arr,0,d)
    n=len(arr)
    rever(arr,d+1,n-1)
    # [4, 3, 2, 1, 8, 7, 6, 5] before added the n ext line
    rever(arr,0,n-1)
    # [5, 6, 7, 8, 1, 2, 3, 4]
    print(arr)
    

v=[1,2,3,4,5,6,7,8]
raar(v,3)

    