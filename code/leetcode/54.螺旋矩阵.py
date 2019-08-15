class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        results = []
        row_num = len(matrix)
        if row_num == 0:
            return results
        line_num = len(matrix[0])
        num = len(matrix)*len(matrix[0])
        direction = 0
        row=0
        line=-1
        while True:
            if direction == 0:
                if line_num <= line+1 or matrix[row][line+1] == '-':
                    direction = 1
                    continue
                else:
                    line += 1
            elif direction == 1:
                if row_num <= row+1 or matrix[row+1][line] == '-':
                    direction = 2
                    continue
                else:
                    row += 1
            elif direction == 2:
                if line-1 < 0 or matrix[row][line-1] == '-':
                    direction = 3
                    continue
                else:
                    line -= 1
            else:
                if row-1 < 0 or matrix[row-1][line] == '-':
                    direction = 0
                    continue
                else:
                    row -= 1
            results.append(matrix[row][line])
            matrix[row][line] = '-'
            if len(results) == num:
                break
        return results