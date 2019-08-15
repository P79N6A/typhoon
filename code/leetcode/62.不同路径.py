class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        records = [[0] * n for _ in range(m)]
        records[0] = [1 for _ in range(n)]
        for i in range(m):
            records[i][0] = 1
        for i in range(1, m, 1):
            for j in range(1, n, 1):
                records[i][j] = records[i-1][j] + records[i][j-1]
        return records[-1][-1]

a = Solution()
print a.uniquePaths(3, 2)