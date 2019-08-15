class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        dice = {}
        is_one = 0
        for i in range(len(s)):
            if s[i] not in dice.keys():
                dice[s[i]] = 1
            else:
                 dice[s[i]] += 1
        for value in dice.values:
            if value % 2 == 0:
                num += value
            else:
                is_one = 1
                num += value - 1
        return num + is_one