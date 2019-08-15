class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        use = 0
        num = 1
        for char in list(S):
            if 100 - use < widths[ord(char)-97]:
                num += 1
                use = 0
            use += widths[ord(char)-97]
        return [num, use]
        