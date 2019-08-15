class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_row = len(grid)
        num_line = len(grid[0])
        sums = [[0 for j in range(num_line)] for i in range(num_row)]
        print(sums)
        for i in range(num_row):
            for j in range(num_line):
                if i==0 and j!=0:
                    sums[i][j]=sums[i][j-1]
                elif j==0 and i!=0:
                    sums[i][j]=sums[i-1][j]
                elif j!=0 and i!=0:
                    sums[i][j]=min(sums[i][j-1],sums[i-1][j])
                sums[i][j]+=grid[i][j]
        return sums[num_row-1][num_line-1]
a=Solution()
print(a.minPathSum([[1,2],[5,6],[1,1]]))
                