class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left,maxlength,zerocount=0,0,0
        for right in range(len(nums)):
            if nums[right]==0:
               zerocount +=1
            while zerocount>k:
                if nums[left]==0:
                    zerocount -=1
                left +=1
            maxlength=max(maxlength,right-left+1)
        return maxlength