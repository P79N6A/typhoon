#树，深度优先遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max_deep = 0
    
    def get_deep(self, root, num):
        if root:
            num += 1
            self.get_deep(root.left, num)
            self.get_deep(root.right, num)
        else:
            self.max_deep = max(self.max_deep, num)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.get_deep(root, 0)
        return self.max_deep

        