def longestCommonPrefix(strs):
	"""
	:type strs: List[str]
	:rtype: str
	"""
	str = ""
	if len(strs)==0:return stra
	for i in range(len(strs[0])):
		isAll = True
		for st in strs:
			if len(st)<=i || st[i]!=strs[0][i]:
				isAll = False
				break
		if isAll:str+=st[i]
		else:break
	return str
		
print(longestCommonPrefix(["12","123"]))