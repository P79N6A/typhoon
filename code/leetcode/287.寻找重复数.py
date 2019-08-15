# 数组、双指针、二分查找

# 二分查找
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        higt = max(nums)
        while low < higt:
            med = (low+higt) // 2
            num = len([i for i in range(len(nums)) if nums[i] <= med])
            if num > med:
                higt = med    
            else:
                low = med+1
        return low 

a = Solution()
b = [1,3,4,2,2]
print(a.findDuplicate(b))
                

# 双指针
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
      