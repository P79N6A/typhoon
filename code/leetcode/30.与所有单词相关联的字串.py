class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        id=-1
        len_nums = len(nums)
        for i in range(len_nums-2,-1):
            if nums[i] < max(nums[i+1:]):
                id=i       
                break
        min_data=100
        min_id=-1
        for i in range(id+1,len_nums):
            if nums[id]<nums[i] and min_data>nums[i]:
                min_id=i
                min_data=nums[i]
        nums[min_id],nums[id]=nums[id],nums[min_id]
        list_num = nums[(id+1):]
        list_num=list_num.sort()
        if id==-1:
            nums = list_num
        else:
            nums = nums[0:id+1] + list_num
        return nums[1]

a=Solution()
print(a.nextPermutation([1,2,3]))      