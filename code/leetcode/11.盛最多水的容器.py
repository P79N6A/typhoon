class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height)-1
        max_data=0
        while start < end:
            max_data = max(max_data, min(height[start], height[end]) * (end-start))
            if height[start] < height[end]:
                start+=1
            else:
                end-=1
        return max_data
            
            
            
        