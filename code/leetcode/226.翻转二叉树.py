# 树
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def reversal(self, root):
        if root:
            root.left,  root.right = root.right,  root.left
            self.reversal(root.left)
            self.reversal(root.right)

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.reversal(root)
        return root
        