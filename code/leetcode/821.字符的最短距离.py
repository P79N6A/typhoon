class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
       class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        s = list(S)
        c_ids = [i for i, c in enumerate(s) if c == C]
        result = []
        id = 0
        len_num = len(c_ids)
        for i in xrange(len(s)):
            if i > c_ids[id] and id<len_num-1:
                id += 1
            if id == 0 and i <= c_ids[id]:
                result.append(c_ids[id]-i)
            elif i >= c_ids[id]:
                result.append(i-c_ids[id])
            else:
                result.append(min(i-c_ids[id-1], c_ids[id]-i))
        return result