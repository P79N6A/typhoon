class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n=len(cost)
        min_cost=0
        sums = [0 for i in range(n)]
        sums[0]=cost[0]
        sums[1]=cost[1]
        for i in range(2,n,1):
            sums[i] = cost[i] + min(sums[i-2], sums[i-1])
        return min(sums[n-1], sums[n-2])
            
a = Solution()
print(a.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
            