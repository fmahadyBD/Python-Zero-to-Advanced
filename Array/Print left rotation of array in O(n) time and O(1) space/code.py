def plro(arr,k):
    n=len(arr)
    m=k%n #it means the k is the not bbounce of index if is it, then it rotaed 
    for i in range(n):
        print(arr[(m+i)%n] ,end=" ")   
    print()


v=[1,2,3,4,5,6,7]
plro(v,2)

# Ans: 3 4 5 6 7 1 2 