#回溯
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left1=n-1
        left2=1
        right1=n-1
        right2=0
        listString = []
        self.DiGui("(", n, listString)
        return listString
    
    def DiGui(self, string, n, listString):
        left2 = string.count('(')
        left1 = n-left2
        right2 = string.count(')')
        right1 = n-1-right2
        if right2==n-1 and left2==n:
            listString.append(string+')')
            return
        if left1>0:
            string += '('
            self.DiGui(string, n, listString)
            string = string[:-1]
        if right1>0 and right2+1<=left2:
            string += ')'
            self.DiGui(string, n, listString)

a = Solution()
print(a.generateParenthesis(3))
