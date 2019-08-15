def search(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""
	len_nums = len(nums)
	if len_nums > 1:
		low = 0
		high = len_nums-2
		data = nums[-1]
		mid = 0
		while low <= high:
			mid = (low + high) // 2
			if data < nums[mid]:
				if nums[mid+1] < data:
					break
				else:
					low = mid+1
			else:
				if nums[mid-1] > data:
					mid = mid-1
					break
				else:
					high = mid-1
		print(mid)
		if data < target:
			low = 0
			high = mid
		else:
			if nums[mid] > target:
				low = mid+1
			else:
				low = mid
			high = len(nums)-1
		print(low,high)
		while low <= high:
			mid = (low + high) // 2
			if target == nums[mid]:
				return mid
			elif target < nums[mid]:
				high = mid-1
			elif target > nums[mid]:
				low = mid+1
	elif len_nums==1 and nums[0]==target:
		return 0 
	return -1

print(search([3,5,1], 1))