class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        pairs = 0

        for i in range(n):
            for j in range(n):
                match = True
                for k in range(n):
                    if grid[i][k] != grid[k][j]:
                        match = False
                        break
                if match:
                   pairs += 1

        return pairs 