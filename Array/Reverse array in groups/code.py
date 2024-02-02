#https://www.geeksforgeeks.org/problems/reverse-array-in-groups0255/1?page=1&category=Arrays&difficulty=Basic&sortBy=submissions
#User function template for Python

class Solution:
    # Function to reverse every sub-array group of size K.
    def reverseInGroups(self, arr, N, K):
        n = len(arr)
        for i in range(0, N, K):
            start = i
            end = min(K + i - 1, n - 1)
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        return arr

