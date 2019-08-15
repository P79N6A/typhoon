def countAndSay(n):
	"""
	:type n: int
	:rtype: str
	"""
	string = "1"
	while n-1:
		string1=""
		i=0
		while i<len(string):
			j=0
			while i+j<len(string) and string[i]==string[j+i]:j+=1
			string1 += str(j) + string[i]
			i+=j
		string = string1
		n-=1
	return string
	
print(countAndSay(5))