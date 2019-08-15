class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum_=0
        i=0
        while i<len(prices):
            max_num=0
            sign=0
            if i==len(prices)-1:
                return sum_
            for j in range(i+1,len(prices)):
                if prices[j]<prices[i]:
                    break
                else:
                    if prices[j]>max_num or max_num==0:
                        sign,max_num =j, prices[j]
                    else:
                        break
            if i+1!=j or j==len(prices)-1:
                sum_ += (max_num-prices[i])
                i=sign+1
            else:
                i+=1
        return sum_
if __name__ == "__main__":
    a = Solution()
    #a.maxProfit([7,1,5,3,6,4])
    print(a.maxProfit([7,6,4,3,1]))