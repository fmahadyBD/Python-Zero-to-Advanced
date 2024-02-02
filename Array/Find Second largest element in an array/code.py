import sys

def second(arr):
    f = -sys.maxsize
    s = -sys.maxsize
    n = len(arr)
    
    if n < 2:
        print("Invalid input")
        return 
    
    for i in range(n):
        if arr[i] > f:
            s = f
            f = arr[i]
        elif arr[i] > s and arr[i] != f:
            s = arr[i]
    
    print(s)

v = [1, 2, 3, 4, 5, 6, 3, 4, 0,8,9]
second(v)
