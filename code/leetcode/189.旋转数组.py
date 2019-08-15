# class Solution:
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         nums[:] = nums[n-k:] + nums[:n-k]

# class Solution:
#     def reverse(self, nums, start, end):
#         while start < end:
#             nums[start], nums[end] = nums[end], nums[start]
#             start, end = start + 1, end - 1

#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         self.reverse(nums, 0, n - 1)
#         self.reverse(nums, 0, k - 1)
#         self.reverse(nums, k, n - 1)

# class Solution:
#     def rotate(self, nums, k):
#         nums_len = len(nums)
#         while k > 0:
#             k-=1
#             previous = nums[nums_len-1]
#             for j in range(nums_len):
#                 nums[j], previous = previous, nums[j]

class Solution:
    def rotate(self, nums, k):
        count = 0
        start = 0
        nums_len = len(nums)
        while count<nums_len:
            current = start
            prev = nums[start]
            next = (current+k) % nums_len
            prev, nums[next] = nums[next], prev 
            current = next
            count+=1
            while start!=current:
                next = (current+k) % nums_len
                prev, nums[next] = nums[next], prev 
                current = next
                count+=1
            start += 1

if __name__ == "__main__":
    test = Solution()
    nums = [1,2,3,4,5,6,7]
    test.rotate(nums, 3)
    print(nums)