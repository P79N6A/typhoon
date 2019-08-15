def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        mi = abs(nums[0]+nums[1]-target+nums[2])
        result=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                if mi>abs(nums[j]+nums[k]-target+nums[i]):
                    mi=abs(nums[j]+nums[k]-target+nums[i])
                    result=nums[j]+nums[k]+nums[i]
                if nums[j]+nums[k]>target-nums[i]:k-=1
                elif nums[j]+nums[k]<target-nums[i]:j+=1
                else : return result
        return result