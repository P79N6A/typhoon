class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        higt = len(nums)-1
        while low < higt:
            med = (low + higt) // 2
            if med==0:
                if nums[med] > nums[med+1]:
                    return 0
                low = med + 1
            elif med==len(nums)-1:
                if nums[med] > nums[med-1]:
                    return len(nums)-1
                higt = med - 1
            elif nums[med-1] < nums[med] and nums[med] > nums[med+1]:
                return med
            elif nums[med-1] > nums[med]:
                higt = med - 1
            else:
                low = med + 1
        return low

a = Solution()
b = [1,2,3]
print(a.findPeakElement(b))