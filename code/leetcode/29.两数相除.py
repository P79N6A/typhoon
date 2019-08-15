class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        operator = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            operator = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        dividend_str = str(dividend)
        dividend = 0
        num_str = ""
        for i in range(len(dividend_str)):
            divi_str = str(dividend) + dividend_str[i]
            dividend = int(divi_str)
            num = 0
            if dividend >= divisor:
                while dividend-divisor>=0:
                    num += 1
                    dividend-=divisor
            num_str += str(num)
        num = int(num_str)
        if operator==-1:
            num=0-num
        if 0-2**31>num or num > 2**31-1:
            return 2**31-1
        return num

a = Solution()
print(a.divide(-2147483648, -1))