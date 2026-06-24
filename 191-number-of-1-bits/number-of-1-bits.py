class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=0
        while n:
            res +=1 if n & 1 else 0
            n >>=1
        return res