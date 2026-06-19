
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type sena90te: str
        :rtype: str
        """
    
        radiant=deque()
        dire=deque()
        n=len(senate)
        for i,value in enumerate(senate):
            if value=="R":
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            r=radiant.popleft()
            d=dire.popleft()
            if r<d:
                radiant.append(r+n)
            else:
                dire.append(d+n)
        return "Radiant" if radiant else "Dire"