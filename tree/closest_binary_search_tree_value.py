"""
270. Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestValue(self, root, target):
        if not root: return None

        return self.findValue(root, target)

    def findValue(self, node, target):
        diff = abs(node.val - target)
        if node.left is None and node.right is None:
            return node.val

        if target > node.val and node.right:
            value = self.findValue(node.right, target)
        if target < node.val and node.left:
            value = self.findValue(node.left, target)

        if abs(value - target) < diff:
            return value
        else:
            return node.val

if __name__ == '__main__':
    sol = Solution()
    ### Test case 1
    """

            19
           / \
          7  20
         /  \
        5   18
    """
    root = TreeNode(19)
    node1 = TreeNode(7)
    node2 = TreeNode(20)
    node3 = TreeNode(5)
    node4 = TreeNode(18)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    sol = Solution()
    result = sol.closestValue(root, 8)
    assert (result == 7)

    """

            35
           / \
          7  100
         /  \
        5   18
    """
    root = TreeNode(35)
    node1 = TreeNode(7)
    node2 = TreeNode(100)
    node3 = TreeNode(5)
    node4 = TreeNode(18)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    sol = Solution()
    result = sol.closestValue(root, 97)
    assert (result == 100)