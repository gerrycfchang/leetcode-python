"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        from collections import Counter
        c = Counter()
        self.inorder(root, c)
        maxnum = max(c.values())
        rlist = []
        for i, value in c.iteritems():
            if value == maxnum:
                rlist.append(i)
        return rlist

    def inorder(self, node, c):
        if not node: return
        self.inorder(node.left, c)
        c[node.value] += 1
        self.inorder(node.right, c)
