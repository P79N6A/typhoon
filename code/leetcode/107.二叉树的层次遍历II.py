# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        liss = []
        lis_TreeNode = []
        lis_TreeNode.append(root)
        while lis_TreeNode:
            nodes = []
            lis_data = []
            for node in lis_TreeNode:
                lis_data.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            liss.append(lis_data)
            lis_TreeNode = nodes
        liss.reverse()
        return liss
            
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

a = Solution()
print(a.levelOrderBottom(root))