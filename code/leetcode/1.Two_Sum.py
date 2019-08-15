def twoSum(nums, target):
	tmp_num = {}
	for i in range(len(nums)):
		if target - nums[i] in tmp_num:
			return (tmp_num[target-nums[i]], i)
		else:
			tmp_num[nums[i]] = i
	return (-1, -1)  
	
def twSum(num, target):
	dict = {}
	for i in range(len(num)):
		x = num[i]
		if target-x in dict:
			return (dict[target-x]+1, i+1)
		dict[x] = i
			
a = 11
arr = [4,5,6,7,8]
print(twSum(arr, a))
			

        
        