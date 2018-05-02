# 114. Flatten Binary Tree to Linked List
# 
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example, given the following tree:
# 
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:
# 
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.seqlist = []

    def __str__(self):
        self.portorder(self)
        return ''.join(str(x) for x in self.seqlist)
    
    def portorder(self, curr):
        if not curr: return
        self.seqlist.append(curr.val)
        self.portorder(curr.left)        
        self.portorder(curr.right)

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def traverse(node):
            if not node: return 
            traverse(node.right)
            traverse(node.left)          
            node.right, node.left = self.prev, None
            self.prev = node
        self.prev = None   
        traverse(root)
        


if __name__ == '__main__':
    sol = Solution()
    # Test case 1:
    #     1
    #    / \
    #   2   3
    
    root  = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)

    root.left = node1
    root.right = node2

    sol.flatten(root)
    assert str(root) == '123'

    # Test case 2:
    #     1
    #    / \
    #   2   5
    #  / \   \
    # 3   4   6
    root  = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(5)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(6)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.right = node5

    sol.flatten(root)
    assert str(root) == '123456'
        