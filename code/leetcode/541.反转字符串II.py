class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s_list = list(s)
        len_s = len(s_list)
        num_k = len_s//(2*k)
        
        for i in range(num_k):
            if i != 0:
                s_list[2*k*i:2*k*i+k] = s_list[2*k*i+k-1:2*k*i-1:-1]
            else:
                s_list[0:k] = s_list[k-1::-1]

        if len_s % (2*k) > k:
            if num_k != 0:
                s_list[2*k*num_k:2*k*num_k+k] = s_list[2*k*num_k+k-1:2*k*num_k-1:-1]
            else:
                s_list[2*k*num_k:2*k*num_k+k] = s_list[2*k*num_k+k-1::-1]
        else:
            if num_k!=0:
                s_list[2*k*num_k:] = s_list[len_s-1:2*k*num_k-1:-1]
            else:
                s_list[2*k*num_k:] = s_list[len_s-1::-1]
        return "".join(s_list)
            
a = Solution()
print(a.reverseStr('abcdefg',2))