import re
import sys
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        print(str)
        strs = re.split("(\d+)", str)
        if len(strs)==1 or '0' > strs[1][0] or strs[1][0] > '9':
            return 0
        else:
            data = float(0)
            if strs[0]== "-":
                if strs[1] == '' or '0' > strs[1][0] or strs[1][0] > '9':
                    return 0
                data = -1 * float(strs[1])
            else:
                if strs[0] != "" and strs[0] != "+":
                    return 0
                data = float(strs[1])
        if -2147483648 > data:
            return -2147483648
        elif 2147483647 < data:
            return 2147483647
        else:
            return int(data)


a=Solution()
print(a.myAtoi("+1"))