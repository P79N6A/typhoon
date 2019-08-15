"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def __init__(self):
        self.max_deep = 0

    def get_deep(self, root, num):
        if root:
            num += 1
            for var in root.children:
                self.get_deep(var, num)
            self.max_deep = max(self.max_deep, num)
            

    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.get_deep(root, 0)
        return self.max_deep
        


    
   
       