# 129. Sum Root to Leaf Numbers
# 
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# 
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# 
# Find the total sum of all root-to-leaf numbers.
# 
# For example,
# 
#     1
#    / \
#   2   3
#  
# 
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# 
# Return the sum = 12 + 13 = 25.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res, total = [], 0
        self.inorder(root, [], res)
        for i in range(len(res)):
            total += int(''.join([str(x) for x in res[i]]))
        return total
        
    def inorder(self, node, path, res):
        if not node: return
        self.inorder(node.left, path+[node.val], res)
        if not node.left and not node.right:
            res.append(path + [node.val])
        self.inorder(node.right, path+[node.val], res)


if __name__ == '__main__':
    sol = Solution()

    ### Test case 1
    """
    Given binary tree [3,9,20,null,null,15,7],

           1
         /   \
        2     3 
    """
    root1  = TreeNode(1)
    node11 = TreeNode(2)
    node12 = TreeNode(3)
    root1.left = node11
    root1.right = node12
    assert sol.sumNumbers(root1) == 25
        