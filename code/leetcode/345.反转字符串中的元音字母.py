class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        end = len(s)-1
        start = 0
        while start < end:
            while start < end and s[start] not in vowels:
                start += 1
            while start < end and s[end] not in vowels:
                end -= 1  
            if s[start] in vowels and s[end] in vowels:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1 
        s = ''.join(s)
        return s

a = Solution()
print(a.reverseVowels('hello'))
            