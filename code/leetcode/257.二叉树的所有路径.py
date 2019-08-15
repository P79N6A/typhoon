# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def get_route(self, root, results, stacks):
        if root.left is None and root.right is None:
            str_lis = ""
            for i in range(len(stacks)):
                str_lis += str(stacks[i].val) + '->'
            str_lis += str(root.val)
            results.append(str_lis)
        if root.left:
            stacks.append(root)
            self.get_route(root.left, results, stacks)
            stacks.pop()
        if root.right:
            stacks.append(root)
            self.get_route(root.right, results, stacks)
            stacks.pop()

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        stacks = []
        results = []
        self.get_route(root, results, stacks)
        return results
        