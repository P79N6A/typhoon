class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum_data=1
        for i in range(1,n,1):
            sum_data=sum_data+i
        return sum_data
            