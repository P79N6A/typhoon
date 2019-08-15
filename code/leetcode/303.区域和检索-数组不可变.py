class NumArray(object):
    sums=[]
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = [0 for i in range(len(nums))]
        if len(nums) != 0:
            self.sums[0]=nums[0]
        for i in range(1,len(nums),1):
            self.sums[i]=self.sums[i-1]+nums[i]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i==0:
            return self.sums[j]
        return self.sums[j]-self.sums[i-1]

obj = NumArray([-2,0,3,-5,2,-1])
param_1 = obj.sumRange(0,2)
print(param_1)