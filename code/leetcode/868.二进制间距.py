class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary = bin(N).replace('0b','')
        print(binary)
        max_space = 0
        previous = -1
        for i, char in enumerate(list(binary)):
            if char == '1':
                if previous != -1:
                    max_space = max(max_space, i-previous)
                previous = i
        return max_space

a = Solution()      
print(a.binaryGap(22))
                
                