def threeSum(nums):
	"""
	:type nums: List[int]
	:rtype: List[List[int]]
	"""
	nums.sort()
	lista =[]
	data =[]
	a=0
	b=0
	for i in range(len(nums)):
		if i==0 or nums[i-1]!=nums[i]:
			j=i+1
			t=len(nums)-1
			while j<t:
				val=nums[i]+nums[j]+nums[t]
				if val==0 and [nums[i],nums[j],nums[t]] not in lista:
					lista.append([nums[i],nums[j],nums[t]])
					j+=1
					t-=1
				elif val<0:
					j+=1
				elif val>0:
					t-=1
	return lista
	
print(threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))