class Solution(object):
    # 动态规划
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max_data = -100
        for i in range(len(nums)):
            sum = max(nums[i], sum+nums[i])
            if max_data < sum:
                max_data = sum
        return max_data
            