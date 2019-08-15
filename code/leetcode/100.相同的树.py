# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_result(self, p, q):
        if p is None and q is None:
            return True
        if p and q and p.val == q.val:
            if self.get_result(p.left, q.left) is False:
                return False
            if self.get_result(p.right, q.right) is False:
                return False
            return True
        else:
            return False
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.get_result(p, q)
        
        