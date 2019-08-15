class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        li=[]
        self.perm(nums, 0, len(nums), li)
        return li
    
    def perm(self, n, begin, end, lis):
        if begin >= end:  
            lis.append(n[:])
        else:  
            i = begin  
            for num in range(begin, end):  
                n[num], n[i] = n[i], n[num]  
                self.perm(n, begin+1, end, lis)  
                n[num], n[i]=n[i], n[num]  

a=Solution()
print(a.permute([1,2,3]))