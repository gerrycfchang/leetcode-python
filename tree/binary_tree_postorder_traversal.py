# 145. Binary Tree Postorder Traversal
# 
# Given a binary tree, return the postorder traversal of its nodes' values.
# 
# For example:
# Given binary tree [1,null,2,3],
# 
#    1
#     \
#      2
#     /
#    3
#  
# 
# return [3,2,1].


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        Solution.res = []
        def postOrder(node):
            if not node: return
            postOrder(node.left)
            postOrder(node.right)
            Solution.res.append(node.val)
        postOrder(root)
        return Solution.res

if __name__ == '__main__':
    sol = Solution()
    
    root  = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.right = node1
    node1.left = node2
    assert sol.postorderTraversal(root) == [3, 2, 1]
        