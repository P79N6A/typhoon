class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '' or s is None:
            return s
        s_reversal = ""
        words = s.split(' ')
        for word in words:
            s_reversal += word[::-1] + " "
        return s_reversal[:-1]
        