# 位运算、数组、分治法
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        data = 0
        for num in nums:
            if count==0:
                count+=1
                data = num
            elif num == data:
                count+=1
            else:
                count-=1
        return data
        