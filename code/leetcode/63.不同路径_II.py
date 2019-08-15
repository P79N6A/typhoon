class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        records = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            records[0][0] = 1
        for i in range(m):
            for j in range(n):
                up = 0
                left = 0
                if obstacleGrid[i][j] == 0:
                    if i != 0:
                        up = records[i-1][j]
                    if j != 0:
                        left = records[i][j-1]
                    if j != 0 or i != 0:
                        records[i][j] = up + left
        return records[-1][-1]

a = Solution()
b = [[1,0]]
print a.uniquePathsWithObstacles(b)