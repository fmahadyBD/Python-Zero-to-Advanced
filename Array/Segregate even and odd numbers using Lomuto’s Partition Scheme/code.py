#this is Lomuto's partision means 2 povit
def arrayEvenAndOdd(arr, n):
    i = -1
    j = 0
    while (j != n):
        if (arr[j] % 2 == 0):
            i = i+1

            # Swapping even and odd numbers
            arr[i], arr[j] = arr[j], arr[i]

        j = j+1

    # Printing segregated array
    for i in arr:
        print(str(i) + " ", end='')
        
v=[1,2,3,4,5,6,7,8]
arrayEvenAndOdd(v,8)