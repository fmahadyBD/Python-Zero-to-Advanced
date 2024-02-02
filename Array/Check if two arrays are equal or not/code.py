#https://www.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1?page=1&category=Arrays&difficulty=Basic&sortBy=submissions

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        A.sort()
        B.sort()
        for i in range(0,N):
            if A[i]!=B[i]:
                return False
        
        return True
