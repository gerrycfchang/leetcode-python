# 872. Leaf-Similar Trees
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """        
        def dfs(node, res):
            if not node: return
            dfs(node.left, res)
            if not node.left and not node.right:
                res.append(node.val)
            dfs(node.right, res)
        ret1, ret2 = [], []
        dfs(root1, ret1)
        dfs(root2, ret2)
        return ret1 == ret2
        

if __name__ == '__main__':
    obj = Solution()

    #      4
    #     / \
    #    2   7
    root1 = TreeNode(4)
    node1 = TreeNode(2)
    node2 = TreeNode(7)
    root1.left = node1
    root1.right = node2
    
    #      3
    #     / \
    #    2   7
    root2 = TreeNode(3)
    node3 = TreeNode(2)
    node4 = TreeNode(7)
    
    root2.left = node3
    root2.right = node4

    assert obj.leafSimilar(root1, root2) == True

