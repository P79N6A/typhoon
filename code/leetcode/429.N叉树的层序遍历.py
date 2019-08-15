"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        liss = []
        lis_nones = []
        lis_nones.append(root)
        while lis_nones:
            lis = []
            nones = []
            lis_nones.clear()
            for lis_none in lis_nones:
                lis.append(lis_none.val)
                nones += lis_none.children
            lis_nones = nones
            liss.append(lis)
        return liss
           
            
        
        