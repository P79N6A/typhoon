# 回溯法
# 深搜+递归
class Solution(object):
	def letterCombinations(self, digits):
			num_alp_table = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
			if len(digits) == 0:
				return []
			path, result = "", []
			begin = 0
			self.helper(digits, begin, path, result, num_alp_table)
			return result
	
	def helper(self, digits, begin, path, result, num_alp_table):
		# 深搜触底，回溯
		if len(path) == len(digits):
			result.append(path)
			return
		# 遍历某个数字代表的所有字母
		for i in num_alp_table[int(digits[begin])]:
			path += i
			# 从下一位开始，到最后的组合情况
			self.helper(digits, begin + 1, path, result, num_alp_table)
			path = path[:-1]

a = Solution()
print(a.letterCombinations("23"))



	 
	