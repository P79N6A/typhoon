class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        re = []
        sum = nums[0]
        for i in range(1, len(nums), 1):
            sum ^= nums[i]
        flag = sum & (~(sum - 1))
        for i in range(0, len(nums), 1):
            if (nums[i] & flag) == 0: 
                re[0] ^= nums[i]
            else: 
                re[1] ^= nums[i]
        return re