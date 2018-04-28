# 199. Binary Tree Right Side View
# 
# Given a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(node, level, dic):
            if not node: return
            inorder(node.left, level+1, dic)
            dic[level].append(node.val)
            inorder(node.right, level+1, dic)
        
        dic, res = defaultdict(list), []
        inorder(root, 1, dic)
        for key in sorted(dic.keys()):
            res.append(dic[key][-1])
        return res

if __name__ == '__main__':
    sol = Solution()
    """
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    """
    root  = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)

    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4
    assert sol.rightSideView(root) == [3, 20, 7]