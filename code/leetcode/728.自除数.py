class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left , right+1):
            ss = set(str(i))
            if '0' not in ss:
                ll = list(ss)
                for j in ll:              
                    if i % int(j) != 0:
                        break
                    elif j == ll[-1]:     
                        res.append(i)
        return res
