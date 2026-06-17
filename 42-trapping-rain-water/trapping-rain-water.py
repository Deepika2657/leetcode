class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0

        highest = max(height)
        midpoint = height.index(highest)

        left_max = height[0]
        for i in range(1, midpoint):
            left_max = max(left_max, height[i])
            total += left_max - height[i]

        right_max = height[-1]
        for i in range(len(height) - 2, midpoint, -1):
            right_max = max(right_max, height[i])
            total += right_max - height[i]

        return total