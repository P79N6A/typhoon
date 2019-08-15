# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.min_data = 99999

    def get_min(self, root, line):
        if root:
            if self.min_data <= line:
                return
        if root.left:
            self.get_min(root.left, line+1)
        if root.right:
            self.get_min(root.right, line+1)
        if root.left is None and root.right is None:
            if self.min_data > line:
                self.min_data = line
    
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.get_min(root, 1)
        return self.min_data

root = TreeNode(1)
root2 = TreeNode(2)

root.left = root2

a = Solution()
print(a.minDepth(root))

        