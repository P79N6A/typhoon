class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None:
            return None
        row_num = len(A[0])
        line_num = len(A)
        results = []
        for i in range(row_num):
            result = []
            for j in range(line_num):
                result.append(A[j][i])
            results.append(result)
        return results  

b = [[1,2,3],[4,5,6]]
a = Solution()
print(a.transpose(b))