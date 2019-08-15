class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if A is None:
            return A
        even = 0
        odd = 1
        num = len(A)
        while even < num and odd < num:
            while even < num and A[even]%2 == 0:
                even += 2
            while odd < num and A[odd]%2 == 1:
                odd += 2    
            if even < num and odd < num:
                A[even], A[odd] =  A[odd], A[even]
        return A
            
            