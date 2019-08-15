# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_tree(self, root, L, R):
        if root.left:
            if root.left.left or root.left.right:
                self.get_tree(root.left, L, R)
        if root.right:
            if root.right.left or root.right.right:
                self.get_tree(root.right, L, R)
        if root.left and root.left.val < L:
            root.left = root.left.right
        if root.right and root.left.val > R:
            root.right = root.left.right

    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        self.get_tree(root, L, R)
        return root
        