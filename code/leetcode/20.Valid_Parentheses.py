def isValid(s):
	"""
	:type s: str
	:rtype: bool
	"""
	arrs=[]
	arr=""
	for ch in s:
		if ch=="[" or ch=="(" or ch=="{":arrs.append(ch)
		else:
			if len(arrs)==0:return False
			else:arr = arrs.pop()
			if not ((arr=="{" and ch=="}") or (arr=="[" and ch=="]") or (arr=="(" and ch==")")):return False
	if len(arrs)==0:return True
	else:return False