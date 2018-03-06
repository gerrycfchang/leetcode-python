# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].


import sys
sys.path.append('../')
from leetCodeUtil import TreeNode

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(node, res):
            if not node: return
            inorder(node.left, res)
            res.append(node.value)
            inorder(node.right, res)
        res = []
        inorder(root, res)
        return res
        
if __name__ == '__main__':
    sol = Solution()
    
    root  = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.right = node1
    node1.left = node2
    assert sol.inorderTraversal(root) == [1, 3, 2]