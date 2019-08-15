class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        min_num=1000
        max_num=0
        sum_num=0
        for i in nums:
            if i>0:
                num+=1
                min_num=min(min_num,i)
                max_num=max(max_num,i) 
                sum_num+=i
        if num!=0:
            if max_num-min_num==num-1:
                if min_num > 1:
                    return 1
                else:
                    return max_num+1
            else:
                return (min_num+max_num)*(num+1)/2-sum_num
        else:
            return 1
        
