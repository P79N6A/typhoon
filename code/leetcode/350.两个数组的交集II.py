class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dices = {}
        results = []
        for num in nums1+nums2:
            dices[num] = 0
        for num in nums1:
            dices[num] += 1
        for num in nums2:
            if dices[num] > 0:
                results.append(num)
                dices[num] -= 1
        return results
                
            