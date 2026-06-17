class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1+str2 !=str2+str1:
            return ""
        def gcd(len1,len2):
            while len2:
                len1,len2=len2,len1%len2
            return len1
        return str1[:gcd(len(str1),len(str2))] 