#https://leetcode.com/problems/search-insert-position/
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s=0
       
        e=len(nums)
        while(s<e):
            mid=(s+e)//2
            if nums[mid]==target:
               return mid
            elif nums[mid]>target:
                e=mid
            else:
                s=mid+1
        return s


        