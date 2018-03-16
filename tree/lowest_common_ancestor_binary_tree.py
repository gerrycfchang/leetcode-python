# 236. Lowest Common Ancestor of a Binary Tree
# 
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# 
# According to the definition of LCA on Wikipedia: 
# "The lowest common ancestor is defined between two nodes v and w as the lowest node in T 
# that has both v and w as descendants (where we allow a node to be a descendant of itself).""
# 
#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4
# For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. 
# Another example is LCA of nodes 5 and 4 is 5, 
# since a node can be a descendant of itself according to the LCA definition.

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
        if root in (None, p, q): return root
        ## parent[0] = left, parent[1] = right
        parent = []
        for kid in (root.left, root.right):
            parent.append(self.lowestCommonAncestor(kid, p, q))
        return root if parent[0] and parent[1] else parent[0] or parent[1]
            
if __name__ == '__main__':
    sol = Solution()
    #         _______3______
    #        /              \
    #     ___5__          ___1__
    #    /      \        /      \
    #    6      _2       0       8
    #          /  \
    #          7   4
    root  = TreeNode(3)
    node1 = TreeNode(5)
    node2 = TreeNode(1)
    node3 = TreeNode(6)
    node4 = TreeNode(2)
    node5 = TreeNode(0)
    node6 = TreeNode(8)
    node7 = TreeNode(7)
    node8 = TreeNode(4)
    
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    node4.left = node7
    node4.right = node8

    res = sol.lowestCommonAncestor(root, node1, node2)
    assert res == root 

    res = sol.lowestCommonAncestor(root, node1, node8)
    assert res == node1