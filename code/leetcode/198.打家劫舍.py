class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        sums = [0 for i in range(len_nums)]
        if len_nums==0:
            return 0
        elif len_nums==1:
            return nums[0]
        elif len_nums==2:
            return max(nums[0], nums[1])
        sums[0] = nums[0] 
        sums[1] = nums[1]   
        sums[2] = nums[2] + nums[0]
        for i in range(3, len_nums, 1):
            sums[i] = nums[i] + max(sums[i-2], sums[i-3])
        return max(sums)

a = Solution()
print(a.rob([2,7,9,3,1]))