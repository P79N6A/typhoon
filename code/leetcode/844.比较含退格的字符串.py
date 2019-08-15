class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack_S = []
        stack_T = []
        for i in range(len(S)):
            if S[i] == '#':
                if stack_S:
                    stack_S.pop()
            else:
                stack_S.append(S[i])
        for i in range(len(T)):
            if T[i] == '#':
                if stack_T:
                    stack_T.pop()
            else:
                stack_T.append(T[i])
        if stack_S == stack_T:
            return True
        return False
            