# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max_num = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.get(root) 
        return self.max_num
    
    def get(self, root):
        sum_left = 0
        sum_right = 0
        if root.left and root.lef.val == root.val:
            sum_left = self.get_max(root.left, 1)
        if root.right and root.right.val == root.val:
            sum_right = self.get_max(root.right, 1)
        self.max_num = max(self.max_num, sum_left + sum_right)
        if root.left:
            self.get(root.left)
        if root.right:
            self.get(root.right)
        
    def get_max(self, root, sum_root):
        right_sum = sum_root
        left_sum = sum_root
        if root.left:
            if root.val == root.left.val:
                left_sum = self.get_max(root.left, sum_root + 1)
        if root.right:
            if root.val == root.right.val:
                right_sum = self.get_max(root.right, sum_root + 1)
        return max(left_sum, right_sum)