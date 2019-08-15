class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums_max = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            sums_max += nums[i]
        return sums_max
        