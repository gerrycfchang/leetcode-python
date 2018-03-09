"""
230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 <= k <= BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        n = [0]
        return self.inorder(root, n, k)

    def inorder(self, node, n, k):
        if not node: return None
        val = self.inorder(node.left, n, k)
        if n[0] == k:
            return val
        n[0] += 1
        if n[0] == k:
            return node.value
        return self.inorder(node.right, n, k)
