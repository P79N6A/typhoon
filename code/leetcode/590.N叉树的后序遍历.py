"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root:
            return []
        lis_datas = []
        stacks = []
        stacks.append(root)
        while stacks:
            node = stacks[-1]
            if node.children:
                a = node.children
                a.reverse()
                stacks += a
                node.children = None
            else:
                lis_datas.append(node.val)
                stacks.pop()
        return lis_datas
        
        