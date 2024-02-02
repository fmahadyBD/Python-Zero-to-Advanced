# def isSubset( a1, a2, n, m):

#     as1=set(a1)
#     as2=set(a2)
#     if as2.issubset(as1):
#         return 'Yes'
#     else:
#         return 'No'
  
def isSubset( a1, a2, n, m):
    for i in range(len(a2)):
        if a2[i] in a1:
            a1.remove(a2[i])
        else:
            return 'No'
    return 'Yes'
   
    #https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1?page=1&category=Arrays&difficulty=Basic&sortBy=submissions