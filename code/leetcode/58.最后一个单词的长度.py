class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip().split(' ')
        return len(list(s[-1]))

a = Solution()
print a.lengthOfLastWord('12')