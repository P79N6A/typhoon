class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        stacks = []
        max_area = 0
        max_row = len(grid)
        max_column = len(grid[0])
        for i in range(max_row):
            for j in range(max_column):
                if grid[i][j] == 1:
                    stacks.append([i, j])
                    grid[i][j] = 0
                    area = 0
                    while stacks:
                        coordinate = stacks.pop()
                        row = coordinate[0]
                        column = coordinate[1]
                        area += 1
                        if row + 1 < max_row and grid[row+1][column] == 1:
                            stacks.append([row+1, column])
                            grid[row+1][column] = 0
                        if column + 1 < max_column and grid[row][column + 1] == 1:
                            stacks.append([row, column + 1])
                            grid[row][column+1] = 0
                        if row > 0 and grid[row-1][column] == 1:
                            stacks.append([row-1, column])
                            grid[row-1][column] = 0
                        if column > 0 and grid[row][column-1] == 1:
                            stacks.append([row, column-1])
                            grid[row][column-1] = 0
                    max_area = max(max_area, area)
        return max_area