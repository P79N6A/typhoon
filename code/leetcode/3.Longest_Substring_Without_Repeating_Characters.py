def lengthOfLongestSubstring(s):
	list = []
	list1 =[]
	maxNum = 0
	for ch in s:
		if len(list)!=0 and ch in list:
			if len(list)>maxNum:
				maxNum=len(list)
			for i in list:
				list1.append(i)
				if i==ch:break
			for i in list1:
				list.remove(i)
			list1 = []
		list.append(ch)
	if len(list)>maxNum:maxNum=len(list)
	return maxNum

print(lengthOfLongestSubstring("pwwkew"))
		