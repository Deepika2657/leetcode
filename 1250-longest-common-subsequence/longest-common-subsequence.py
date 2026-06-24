class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
    
        dp=[0]*len(text1)
        long=0
        for c in text2:
            currentlen=0
            for i,val in enumerate(dp):
                if currentlen<val:
                    currentlen=val
                elif c ==text1[i]:
                    dp[i]=currentlen+1
                    long=max(long,currentlen+1)
        return long

        