# 位运算、哈希表
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rec = 0
        for i in range(len(nums)):
            rec  = rec ^ nums[i]
        return rec
        