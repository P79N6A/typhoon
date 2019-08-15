# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return []
        stacks = []
        stacks.append(root)
        sum_rows = []
        while stacks:
            sum_stack = 0
            nodes = []
            num = len(stacks)
            for treenode in stacks:
                sum_stack += treenode.val
                if treenode.left:
                    nodes.append(treenode.left)
                if treenode.right:
                    nodes.append(treenode.right)
            stacks = nodes
            sum_rows.append(sum_stack*1.0/num)
        return sum_rows
                
            