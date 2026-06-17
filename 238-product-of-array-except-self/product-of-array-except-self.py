class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[0]*len(nums)
        p=1
        for i in range(len(nums)):
            result[i]=p
            p *=nums[i]
        s=1   
        for i in range(len(nums)-1,-1,-1):
            result[i] *=s
            s *=nums[i]
        return result