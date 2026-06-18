class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,zero,res=0,0,0
        for right in range(len(nums)):
            if nums[right]==0:
                zero +=1
            while zero >1:
                if nums[left]==0:
                    zero -=1
                left +=1
            res=max(res,right-left)
        return res