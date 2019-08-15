class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == '' or word is None:
            return False
        if word == word.upper() or word == word.capitalize() or word == word.lower():
            return True
        else:
            return False