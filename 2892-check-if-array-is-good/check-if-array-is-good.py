class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    
        
        nums.sort()
        
        n = nums[-1]
        
        # Check size
        if len(nums) != n + 1:
            return False
        
        # Check numbers from 1 to n-1
        for i in range(1, n):
            
            if nums[i - 1] != i:
                return False
        
        # Last two elements should be n
        return nums[-1] == n and nums[-2] == n