class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t = list(t)
        for i in range(len(s)):
            t.remove(s[i])
        return t[0]

a = Solution()
print(a.findTheDifference("123", "1234"))