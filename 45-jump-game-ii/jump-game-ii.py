class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jump, des, pos = 0, 0, 0
        for i in range(len(nums)-1):
            des = max(des, i + nums[i])
            if(i >= des):
                return -1
            if(pos == i):
                pos = des
                jump += 1
        return jump
        