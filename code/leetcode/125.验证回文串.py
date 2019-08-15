class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s)-1
        result = True
        while start < end:
            while start < end and not (65 <= ord(s[start]) <= 90 or 97 <= ord(s[start]) <= 122 or 48 <= ord(s[start]) <= 57):
                start += 1
            while start < end and not (65 <= ord(s[end]) <= 90 or 97 <= ord(s[end]) <= 122 or 48 <= ord(s[end]) <= 57):
                end -= 1
            if start < end and s[start].lower() != s[end].lower():
                result = False
                break
            else:
                start += 1
                end -= 1
        return result

a='`'
#print(ord(a))
if not (65 <= ord(a) <= 122 or 48 <= ord(a) <= 57):
    print("!!!")

b = r"`l;`` 1o1 ??;l`"
a = Solution()
print(a.isPalindrome(b))
                