# 623. Add One Row to Tree
# 
# Example 1:
# Input: 
# A binary tree as following:
#        4
#      /   \
#     2     6
#    / \   / 
#   3   1 5   
# 
# v = 1
# 
# d = 2
# 
# Output: 
#        4
#       / \
#      1   1
#     /     \
#    2       6
#   / \     / 
#  3   1   5   
# 
# Example 2:
# Input: 
# A binary tree as following:
#       4
#      /   
#     2    
#    / \   
#   3   1    
# 
# v = 1
# 
# d = 3
# 
# Output: 
#       4
#      /   
#     2
#    / \    
#   1   1
#  /     \  
# 3       1


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.seqlist = []

    def __str__(self):
        self.inorder(self)
        return ' '.join(str(x) for x in self.seqlist)
    
    def inorder(self, curr):
        if not curr: return
        self.inorder(curr.left)
        self.seqlist.append(curr.val)
        self.inorder(curr.right)

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root
        else:
            self.inorder(root, 1, v, d)
            newRoot = root
        return newRoot

    def inorder(self, node, level, v, d):
        if not node: return
        self.inorder(node.left, level+1, v, d)
        if level == d-1:            
            newLeftNode = TreeNode(v)
            newLeftNode.left = node.left
            node.left = newLeftNode
            newRightNode = TreeNode(v)
            newRightNode.right = node.right
            node.right = newRightNode
            return
        self.inorder(node.right, level+1, v, d)


if __name__ == '__main__':
    sol = Solution()
    
    #    1
    #   / \
    #  2   3
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.left = node1
    root.right = node2

    #     1
    #    / \
    #   4   4
    #  /     \
    # 2       3
    expRoot = TreeNode(1)
    node11 = TreeNode(4)
    node12 = TreeNode(4)
    node21 = TreeNode(2)
    node22 = TreeNode(3)
    expRoot.left = node11
    expRoot.right = node12
    node11.left = node21
    node12.right = node22
    
    assert str(sol.addOneRow(root, 4, 2)) == str(expRoot)        