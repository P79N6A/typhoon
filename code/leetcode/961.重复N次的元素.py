class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        datas = []
        for a in A:
            if a in datas:
                return a
            datas.append(a)