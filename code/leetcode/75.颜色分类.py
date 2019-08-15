class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums)-1
        while start < end:
            while start < end and nums[start] == 0:
                start += 1
            while start < end and nums[end] != 0:
                end -= 1
            nums[start], nums[end] = nums[end], nums[start]
        start = 0
        end = len(nums)-1
        while start < end:
            while start < end and nums[start] != 2:
                start += 1
            while start < end and nums[end] == 2:
                end -= 1
            nums[start], nums[end] = nums[end], nums[start]
         
        