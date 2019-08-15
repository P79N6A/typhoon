# 二分查找

import math
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        higt = math.ceil(num / 2)
        print(higt)
        low = 1
        while low <= higt:
            med = (low + higt)//2
            t = med**2
            if num == t:
                return True
            elif num > t: 
                low = 1 + med
            else:
                higt = med - 1
        return False

a = Solution()
print(a.isPerfectSquare(214748364721474836))
                
            
        