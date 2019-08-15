class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis=[]
        id=0
        max_data=0
        num=0
        i=0
        while i < len(nums):
            lis = nums[i+1:i+nums[i]+1]
            max_data=0
            if len(lis)==0:
                return num
            if i+nums[i]>=len(nums)-1:
                return num+1
            for j in range(len(lis)):
                if max_data <= i+j+lis[j]:
                    max_data = i+j+lis[j]
                    id=i+j+1
            num+=1
            i=id
        return num

a=Solution()
print(a.jump([2,3,1]))
                
                