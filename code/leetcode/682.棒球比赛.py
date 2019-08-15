class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        lis = []
        for char in ops:
            if char == '+':
                lis.append(lis[-1]+lis[-2])
            elif char == 'D':
                lis.append(lis[-1]*2)
            elif char == 'C':
                lis.pop()
            else:
                lis.append(int(char))
        return sum(lis)
                
