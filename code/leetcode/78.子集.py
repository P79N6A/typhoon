# 位运算
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        hash = 1
        subsize = 2**len(nums)
        while hash<subsize:
            temp = []
            for k in range(0, len(nums), 1):
                a = 1<<k
                if a & hash:
                    temp.append(nums[k])
            ret.append(temp)
        return ret