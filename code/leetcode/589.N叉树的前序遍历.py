"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        preorders = []
        stack = []
        if root is None:
            return preorders
        stack.append(root)
        while stack:
            curr = stack.pop()
            preorders.append(curr.val)
            if curr.children:
                curr.children.reverse()
                stack += curr.children
        return preorders
        