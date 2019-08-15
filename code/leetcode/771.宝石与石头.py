class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        num = 0
        dices = {}
        for i in range(len(S)):
            dices[S[i]] = 0
        for i in range(len(J)):
            dices[J[i]] = 1
        for i in range(len(S)):
            if dices[S[i]] == 1:    
                num+=1
        return num