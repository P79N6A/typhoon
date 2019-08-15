class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        num=0
        sum_data=0
        for i in range(2, len(A), 1):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                num+=1
            else:
                num=0
            sum_data+=num
        return sum_data

a=Solution()
print(a.numberOfArithmeticSlices([1,2,3,4,5,6]))