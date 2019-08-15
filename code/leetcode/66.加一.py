class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string=""
        for i in digits:
            string+=str(i)
        s = list(str(int(string)+1))
        digs = []
        for i in s:
            digs.append(int(i))
        return digs

a = Solution()
print(a.plusOne([1,2,3]))
        