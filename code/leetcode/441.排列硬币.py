import math
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        high = math.ceil(n/2)
        low = 1

        while low <= high:
            med = (high + low) // 2
            t = (1 + med) * med // 2
            if t == n:
                return int(med)
            elif t > n:
                high = med - 1
            else:
                low = med + 1
        return int(high)  

a = Solution()
print(a.arrangeCoins(1))