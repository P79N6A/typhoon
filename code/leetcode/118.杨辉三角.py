class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        for i in range(rowIndex+1):
            raw_lis=[]
            for j in range(i+1):
                if i != 0:
                    if j==0:
                        raw_lis.append(raw[j])
                    elif j==i:
                        raw_lis.append(raw[j-1])
                    else:
                        raw_lis.append(raw[j]+raw[j-1])
                else:
                    raw_lis.append(1)
            raw = raw_lis
        return raw
a = Solution()
print(a.generate(3))