class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,h=0,len(nums)-1
        while l<h:
            m=(l+h)//2
            if nums[m]<nums[m+1]:
                l=m+1
            else:
                h=m
        return h