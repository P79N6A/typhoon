# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def merge(self, t1, t2):
        t1.val += t2.val

        if t1.left and t2.left:
            self.merge(t1.left, t2.left)
        elif t1.left is None and t2.left:
            t1.left = t2.left

        if t1.right and t2.right:
            self.merge(t1.right, t2.right)
        elif t1.right is None and t2.right:
            t1.right = t2.right

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            self.merge(t1, t2)
        elif t1 is None and t2:
            return t2
        return t1
        