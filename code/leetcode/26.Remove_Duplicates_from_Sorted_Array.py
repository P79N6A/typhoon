def removeDuplicates(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	if len(nums)==0: return 0
	num = 1
	xSign = 0
	for i in range(1,len(nums)):
		if nums[i] != nums[xSign]:
			xSign+=1
			nums[xSign]=nums[i]
			num+=1
	nums = nums[0:xSign+1]
	return nums

print(removeDuplicates([1,1,2]))
			
		