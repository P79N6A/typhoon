class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num = int(a, 2) + int(b, 2)
        ans = bin(num)
        return ans[2:]



a = Solution()
print a.lengthOfLastWord('12')