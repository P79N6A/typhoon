def fourSum(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[List[int]]
	"""
	nums.sort()
	lista =[]
	for a in range(len(nums)-3):
		for i in range(a+1,len(nums)-2):
			if i==a+1 or nums[i-1]!=nums[i]:
				start=i+1
				end=len(nums)-1
				while start<end:
					val= nums[a]+nums[i]+nums[start]+nums[end]
					if val==target:
						if [nums[a],nums[i],nums[start],nums[end]] not in lista:
							lista.append([nums[a],nums[i],nums[start],nums[end]])
						start+=1
						end-=1
					elif val<target:
						start+=1
					elif val>target:
						end-=1
	return lista
	
print(fourSum([-3,-2,-1,0,0,1,2,3],0))