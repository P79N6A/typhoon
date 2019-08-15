class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        len_nums = len(nums)
        lis = []
        for num in findNums:
            max_num = -1
            for i in range(nums.index(num) + 1, len_nums, 1):
                if nums[i] > num:
                    max_num = nums[i]
                    break
            lis.append(max_num)
        return lis