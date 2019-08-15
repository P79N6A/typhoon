class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        li=[]
        self.perm(nums, 0, len(nums), li)
        return li
    
    def perm(self, n, begin, end, lis):
        if begin >= end:
            if n[:] not in lis:
                lis.append(n[:])
        else:  
            i = begin  
            for num in range(begin, end):  
                n[num], n[i] = n[i], n[num]  
                self.perm(n, begin+1, end, lis)  
                n[num], n[i]=n[i], n[num]  

a=Solution()
print(a.permuteUnique([1,2,3]))