class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for lis in A:
            lis.reverse()
            for i in range(len(lis)):
                lis[i] = lis[i] ^ 1
        return A 

a = Solution()
print(a.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))