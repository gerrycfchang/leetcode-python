# 235. Lowest Common Ancestor of a Binary Search Tree
# 
# Given a binary search tree (BST), 
# find the lowest common ancestor (LCA) of two given nodes in the BST.
# 
# According to the definition of LCA on Wikipedia: 
# "The lowest common ancestor is defined between two nodes v and w as the lowest node in T 
# that has both v and w as descendants (where we allow a node to be a descendant of itself)."
# 
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. 
# Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
        
if __name__ == '__main__':
    sol = Solution()
    #         _______6______
    #        /              \
    #     ___2__          ___8__
    #    /      \        /      \
    #    0      _4       7       9
    #          /  \
    #          3   5
    root  = TreeNode(6)
    node1 = TreeNode(2)
    node2 = TreeNode(8)
    node3 = TreeNode(0)
    node4 = TreeNode(4)
    node5 = TreeNode(8)
    node6 = TreeNode(7)
    node7 = TreeNode(9)
    node8 = TreeNode(3)
    node9 = TreeNode(5)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node6
    node2.right = node7
    node4.left = node8
    node4.right = node9

    res = sol.lowestCommonAncestor(root, node1, node4)
    exp = node1
    assert res == exp 

    res = sol.lowestCommonAncestor(root, node1, node2)
    assert res == root