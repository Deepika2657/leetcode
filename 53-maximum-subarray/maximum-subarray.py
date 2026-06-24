class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
    
        n=len(nums)
        res=nums[0]
        for i in range(n):
            curr=0
            for j in range(i,n):
                curr +=nums[j]
                res=max(res,curr)
        return res
        """
        res = nums[0]
        total = 0

        for n in nums:
            if total < 0:
                total = 0

            total += n
            res = max(res, total)
        
        return res