# 144. Binary Tree Preorder Traversal
# 
# Given a binary tree, return the preorder traversal of its nodes' values.
# 
# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        Solution.res = []
        def preorder(node):
            if not node: return
            Solution.res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return Solution.res
        

if __name__ == '__main__':
    sol = Solution()
    
    root  = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.right = node1
    node1.left = node2
    assert sol.preorderTraversal(root) == [1, 2, 3]