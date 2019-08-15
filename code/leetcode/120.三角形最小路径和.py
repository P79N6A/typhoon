class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        sum=0
        num=len(triangle)
        id=0
        n=0
        self.next_data(id, sum, n, num, triangle)
        return sum
        

    def next_data(self, id, sum, n, num, triangle):
        for i in range(id, n):
            self.next_data(i, sum, n+1, num, triangle)
            