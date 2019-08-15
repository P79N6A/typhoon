# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):



    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        data = root.val
        stack = [root]
        while stack:
            if root:
                stack.append(root.left)
                root = root.left
            else:
                root = stack.pop()
                if root.val != data:
                    return False
                root = root.right
        return True

    midOrder(node * t)
    {
    // 用于储存遍历的元素
    stack < node * > sta;
    while (t | |  !sta.empty() )
    {
    if (t != nullptr)
    {
        sta.push(t);
    t = t->left;
    }
    else
    {
        t = sta.top();
    sta.pop();
    cout << t->val << " ";
    t = t->right;
    }
    }

    ---------------------
    作者：疯狂的小阿咪
    来源：CSDN
    原文：https: // blog.csdn.net / qq_27704269 / article / details / 52566998
    版权声明：本文为博主原创文章，转载请附上博文链接！




