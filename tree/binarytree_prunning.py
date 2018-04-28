# 814. Binary Tree Pruning
# 
# We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.
# 
# Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
# 
# (Recall that the subtree of a node X is X, plus every node that is a descendant of X.)


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.seqlist = []

    def __str__(self):
        self.inorder(self)
        return ''.join(str(x) for x in self.seqlist)
    
    def inorder(self, curr):
        if not curr: return
        self.inorder(curr.left)
        self.seqlist.append(curr.val)
        self.inorder(curr.right)

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(node):
            if not node: return 0
            leftVal = inorder(node.left)
            rightVal= inorder(node.right)
            if leftVal == 0:
                node.left = None
            if rightVal == 0:
                node.right = None
            return leftVal + rightVal + node.val
        inorder(root)
        return root


if __name__ == '__main__':
    sol = Solution()
    """
    #     1
    #    / \
    #   0   1
    #     /  \
    #    0    1
    """
    root  = TreeNode(1)
    node1 = TreeNode(0)
    node2 = TreeNode(1)
    node3 = TreeNode(0)
    node4 = TreeNode(1)

    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4
    assert str(sol.pruneTree(root)) == '111'
    