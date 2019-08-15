class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        left_max = right_max = res = 0
        left, right = 0, len(height) - 1
 
        while left < right:
            if height[left] < height[right]:  # 左指针操作
                if height[left] < left_max:
                    res += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1  # 移动左指针
            else:
                if height[right] < right_max:  # 右指针操作
                    res += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1  # 移动右指针
        return res
