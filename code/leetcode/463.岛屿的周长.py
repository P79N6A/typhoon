class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    perimeter += 4
                    if j<len(grid[i])-1 and grid[i][j+1]==1:
                        perimeter -= 2
                    if i<len(grid)-1 and grid[i+1][j]==1:
                        perimeter -= 2
        return perimeter