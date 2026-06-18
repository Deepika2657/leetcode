class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        a=[]
        a=list(set(nums1)-set(nums2))
        b=[]
        b=list(set(nums2)-set(nums1))
        res.append(a)
        res.append(b)
        return res