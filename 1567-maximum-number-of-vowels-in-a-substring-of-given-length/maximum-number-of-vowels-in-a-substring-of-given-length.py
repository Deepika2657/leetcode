class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
    
        vowels=set('aeiou')
        count=sum(1 for i in range(k) if s[i] in vowels)
        maxx=count
        for i in range(k,len(s)):
            if s[i-k] in vowels:
                count -=1
            if s[i] in vowels:
                count +=1
            if count > maxx:
                max=count
            if count==k:
                return count
        return maxx
        """
        max_cnt = 0
        vowels = ['a','e','i','o','u']
        curr_cnt=0

        # first window count
        for i in range(k):
            if s[i] in vowels:
                curr_cnt+=1

        max_cnt = curr_cnt

        # Slide the window

        for i in range(k,len(s)):
            if s[i] in vowels:
                curr_cnt+=1

            if s[i-k] in vowels:
                curr_cnt -= 1
            
            max_cnt = max(max_cnt,curr_cnt)

        return max_cnt