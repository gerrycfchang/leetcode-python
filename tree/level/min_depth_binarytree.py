# 111. Minimum Depth of Binary Tree
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path 
# from the root node down to the nearest leaf node.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leaflist = []
        def inorder(node, level):
            if not node: return
            inorder(node.left, level + 1)
            if not node.left and not node.right:
                leaflist.append(level)
            inorder(node.right, level + 1)
        inorder(root, 1)
        return min(leaflist) if root else 0

if __name__ == '__main__':
    sol = Solution()
    """
    #     1
    #      \
    #       3
    #      / 
    #     2   
    """
    root  = TreeNode(1)
    node1 = TreeNode(3)
    node2 = TreeNode(2)
    root.right = node1
    node1.left = node2
    assert (sol.minDepth(root) == 3)
    assert (sol.minDepth(None) == 0)
    assert (sol.minDepth(TreeNode(0)) == 1)
            
        