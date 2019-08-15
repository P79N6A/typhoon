class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        higt = len(nums)-1
        low = 0
        while low <= higt:
            med = (low+higt)//2
            if nums[med] == target:
                return med
            elif nums[med] > target:
                higt = med - 1
            else:
                low = med + 1
        return -1