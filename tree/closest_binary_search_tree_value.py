"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

"""

class Solution(object):
    def closestValue(self, root, target):
        if not root: return None

        return self.findValue(root, target)

    def findValue(self, node, target):
        diff = abs(node.value - target)
        if node.left is None and node.right is None:
            return node.value


        if target > node.value and node.right:
            value = self.findValue(node.right, target)
        if target < node.value and node.left:
            value = self.findValue(node.left, target)

        if abs(value - target) < diff:
            return value
        else:
            return node.value
