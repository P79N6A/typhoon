def searchRange(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	li=[]
	di=-1
	gao=-1
	for i in range(len(nums)):
		if nums[i]==target:
			di=i
			break
	if di!=-1
		for i in range(len(nums)-1,-1,-1):
			if nums[i]==target:
			gao=i
			break
	li.append(di)
	li.append(gao)
	return li