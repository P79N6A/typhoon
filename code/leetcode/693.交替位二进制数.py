class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n%2 == 0:
            data=2
        else:
            data=1
        i=0
        while n > 0:
            n -= (4**i)*data
            i+=1
        if n==0:
            return True
        else:
            return False



a = Solution()
print a.lengthOfLastWord('12')