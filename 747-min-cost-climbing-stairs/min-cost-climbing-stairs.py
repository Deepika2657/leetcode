class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0
        curr=0
        dp0=cost[0]
        if len(cost)>=2:
            dp1=cost[1]
        for i in range(2,len(cost)):
            curr=cost[i]+min(dp0,dp1)
            dp0=dp1
            dp1=curr
        return min(dp0,dp1)