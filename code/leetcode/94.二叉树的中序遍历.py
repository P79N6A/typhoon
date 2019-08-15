# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lis=[]
        self.order(root, lis)
        return lis
        
        
    def order(self, root, lis):
        if root:
            self.order(root.left, lis)
            lis.append(root.val)
            self.order(root.right, lis)
        