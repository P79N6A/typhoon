class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        lis=[]
        num=0
        max_num=0
        id=-1
        for i in range(len(s)):
            if s[i]=='(':
                lis.append(i)   
            else:
                if len(lis) == 0:
                    max_num=max(max_num, num)
                    num=0
                    id=i
                else:
                    lis.pop()
                    num+=2
        if id == -1:
            lis.insert(0,-1)
            lis.insert(len(lis),len(s))
        elif id != -1 and len(lis)==0:
            max_num=max(max_num, num)
        else:
            lis.insert(0,id)
            lis.insert(len(lis),len(s))
        print(lis)
        for i in range(len(lis)-1,0,-1):
            max_num = max(max_num, lis[i]-lis[i-1]-1)
        return max_num

a = Solution()
print(a.longestValidParentheses("()"))