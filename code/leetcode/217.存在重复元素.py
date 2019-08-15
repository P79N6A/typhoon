class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None:
            return False
        hashs = {}
        for num in nums:
            hashs[num] = 0
        for num in nums:
            hashs[num] += 1
        for li in hashs.keys():
            if hashs[li] > 1:
                return True
        return False

a = Solution()
print(a.containsDuplicate([1,2,3,1]))
            