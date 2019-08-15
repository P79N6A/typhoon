class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        nums={}
        carry=0
        data_str=""
        len_num1 = len(num1)
        len_num2 = len(num2)
        for i in range(len_num1):
            for j in range(len_num2):
                data=int(num1[i])*int(num2[j])
                digit=len_num1-i+len_num2-j
                if digit in nums.keys:
                    nums[digit]+=data
                else:
                    nums[digit]=data
        for i in nums.keys:
            data = nums[i]+carry
            data_str = str(data%10) + data_str
            carry = data/10
        if carry != 0:
            data_str = str(carry) + data_str
        if data_str[0]=='0':
            return '0'
        return data_str
        