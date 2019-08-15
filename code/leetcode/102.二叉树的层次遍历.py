# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        heads = [root]
        liss = []
        while heads:
            lis = []
            heads_child = []
            for head in heads:
                lis.append(head.val)
                if head.left:
                    heads_child.append(head.left)
                if head.right:
                    heads_child.append(head.right)
            liss.append(lis)
            heads = heads_child
        return liss
                
                