import copy
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        liss=[]
        lis=[]
        last_lis=[([1] * n) for i in range(n)]
        self.huanghou(0, last_lis, lis, liss, n)
        return liss
        
    def huanghou(self, row, last_lis, lis, liss, n):
        if row >= n:
            liss.append(lis)
            return
        if sum(last_lis[row])==0:
            return
        for i in range(n):
            if last_lis[row][i]==1:
                lis.append(i)
                last_li=copy.deepcopy(last_lis)
                id=0
                for j in range(row, n, 1):
                    if i+id < n:
                        last_li[j][i+id]=0
                    if i-id >= 0:
                        last_li[j][i-id]=0
                    last_li[j][i]=0
                    id+=1
                id=0
                for j in range(row, -1, -1):
                    if i+id < n:
                        last_li[j][i+id]=0
                    if i-id >= 0:
                        last_li[j][i-id]=0
                    last_li[j][i]=0                    
                    id+=1
                print("!",row,lis)
                self.huanghou(row+1, last_li, lis, liss, n)
                print("$",lis)
                lis = lis[:-1]
                print("@",row,lis)
        return
a = Solution()
print(a.solveNQueens(4))
            

        

    