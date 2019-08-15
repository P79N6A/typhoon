class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        len_nums = len(nums)
        time = 0
        while time < len_nums:
            if nums[i] == 0:
                for j in range(i, len_nums-1, 1):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
            else:
                i += 1
            time += 1