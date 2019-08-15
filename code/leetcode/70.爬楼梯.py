class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        num=0
        sums = [0 for i in range(n)]
        sums[0]=1
        sums[1]=2
        for i in range(2,n,1):
            sums[i] = sums[i-2]+sums[i-1]
        return sums[n-1]
            
a = Solution()
print(a.climbStairs(3))
            