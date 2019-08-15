class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(A)-1
        while i<j:
            while i<j and A[i]%2==0:
                i+=1
            while i<j and A[j]%2==1:
                j-=1
            A[i], A[j] = A[j], A[i]
        return A

        