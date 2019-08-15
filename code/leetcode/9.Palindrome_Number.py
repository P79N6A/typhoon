def isPalindrome(x):
	"""
	:type x: int
	:rtype: bool
	"""
	if x < 0:return False
	tmp = x
	y = 0
	while tmp > 0:
		y = y*10 + tmp%10
		tmp = int(tmp/10)
	return y == x

print(isPalindrome(121))