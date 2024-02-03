class Solution(object):
    def merge(self, nums1, n, nums2, m):
        # Append elements from nums2 to nums1
        for i in range(m):
            nums1[n+i]=nums2[i]
        nums1.sort()
        return nums1
# https://leetcode.com/problems/merge-sorted-array/