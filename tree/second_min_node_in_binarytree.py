# 671. Second Minimum Node In a Binary Tree
# 
# Given a non-empty special binary tree consisting of nodes with the non-negative value, 
# where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, 
# then this node's value is the smaller value among its two sub-nodes.
# 
# Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
# 
# If no such second minimum value exists, output -1 instead.
# 
# Example 1:
# Input: 
#     2
#    / \
#   2   5
#      / \
#     5   7
# 
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
# Example 2:
# Input: 
#     2
#    / \
#   2   2
# 
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest value.# 


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(curr, value, secMin):
            if not curr: return float('inf')
            leftValue = inorder(curr.left, value, secMin)
            if curr.val > value and curr.val < secMin[0]:
                secMin[0] = curr.val
            rightValue = inorder(curr.right, value, secMin)
            return min(leftValue, rightValue, secMin[0])
        secMin = [float('inf')]
        res = inorder(root, root.val, secMin)
        return res if res != float('inf') else -1
            
if __name__ == '__main__':
    sol = Solution()
    
    root  = TreeNode(2)
    node1 = TreeNode(2)
    node2 = TreeNode(5)
    root.left = node1
    root.right = node2
    assert sol.findSecondMinimumValue(root) == 5

    root  = TreeNode(2)
    node1 = TreeNode(2)
    node2 = TreeNode(5)
    node3 = TreeNode(5)
    node4 = TreeNode(7)
    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4
    assert sol.findSecondMinimumValue(root) == 5

    root  = TreeNode(2)
    node1 = TreeNode(2)
    node2 = TreeNode(2)
    root.left = node1
    root.right = node2
    assert sol.findSecondMinimumValue(root) == -1

    root  = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.left = node1
    root.right = node2
    assert sol.findSecondMinimumValue(root) == 2

    root  = TreeNode(1)
    node1 = TreeNode(1)
    node2 = TreeNode(3)

    node11 = TreeNode(1)
    node12 = TreeNode(1)
    node21 = TreeNode(3)
    node22 = TreeNode(4)

    node111 = TreeNode(3)
    node112 = TreeNode(1)
    node121 = TreeNode(1)
    node122 = TreeNode(1)

    node1111 = TreeNode(3)
    node1112 = TreeNode(3)
    node1121 = TreeNode(1)
    node1122 = TreeNode(6)

    node1211 = TreeNode(2)
    node1212 = TreeNode(1)

    root.left = node1
    root.right = node2
    node1.left = node11
    node1.right = node12
    node2.left = node21
    node2.right = node22

    node11.left = node111
    node11.right = node112
    node12.left = node121
    node12.right = node122

    node111.left = node1111
    node111.right = node1112
    node112.left = node1121
    node112.right = node1122
    node121.left = node1211
    node121.right = node1212

    assert sol.findSecondMinimumValue(root) == 2




