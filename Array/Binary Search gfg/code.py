#https://www.geeksforgeeks.org/problems/binary-search-1587115620/1?page=1&category=Arrays&difficulty=Basic&sortBy=submissions

class Solution:	
	def binarysearch(self, arr, n, k):
		# code here
        s=0
        e=n-1
        while s<=e:
            m=(s+e)//2
            if arr[m]==k:
                return m
            elif arr[m]<k:
                s=m+1
            else:
                e=m-1
        return -1
            