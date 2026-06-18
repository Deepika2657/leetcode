class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq={}
        for i in  arr:
            freq[i]=freq.get(i,0)+1   
        return len(freq)==len(set(freq.values()))
        
        