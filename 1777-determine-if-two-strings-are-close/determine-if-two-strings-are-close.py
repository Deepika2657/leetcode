class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        f1=Counter(word1)
        f2=Counter(word2)
        s1=sorted(f1.values())
        s2=sorted(f2.values())
        keys_match=set(f1.keys())==set(f2.keys())
        return s1==s2 and keys_match