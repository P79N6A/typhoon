#注意 int范围 2147483647 -2147483648

def reverse(x):
	"""
	:type x: int
	:rtype: int
	"""
	strData=""
	if str(x)[0]=="-":isFu=True
	else:isFu=False
	for ch in str(x):
		if ch!="-":
			strData = ch + strData
	if isFu:strData = "-" + strData
	if int(strData)>2147483647 or int(strData)<-2147483648:
		return 0
	else:int(strData)
	
print(reverse(1534236469))