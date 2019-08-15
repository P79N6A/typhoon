def longestPalindrome(s):
	"""
	:type s: str
	:rtype: str
	"""
	max_len=0
	state=0
	dp=[([False] * len(s)) for i in range(len(s))]
	for i in range(len(s)):
	    for j in range(i+1):
		if i-j<2:
			dp[j][i]=(s[i]==s[j])
		else:
			dp[j][i]=(s[i]==s[j] and dp[j+1][i-1])
		if dp[j][i] and max_len<(i-j+1):
		    max_len=i-j+1
		    state=j
	return s[state:state+max_len]
print longestPalindrome("cbbd")
		
		
