# 637. Average of Levels in Binary Tree
# 
# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. 
# Hence return [3, 14.5, 11].


# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res, c = [], collections.defaultdict(list)
        
        def inorder(curr, c, level):
            if not curr: return
            inorder(curr.left, c, level+1)
            c[level].append(curr.val)
            inorder(curr.right, c, level+1)
        inorder(root, c, 0)
        for key in c.keys():
            res.append(float(sum(c[key]))/float(len(c[key])))
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

    assert (sol.averageOfLevels(root) == [3.0, 14.5, 11.0])
            