class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        maxal,currental=0,0
        for g in gain:
            currental +=g
            maxal=max(maxal,currental)
        return maxal
            