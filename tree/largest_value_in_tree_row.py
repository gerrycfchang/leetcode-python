# 515. Find Largest Value in Each Tree Row
# 
# You need to find the largest value in each row of a binary tree.
# 
# Example:
# Input: 
# 
#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 
# 
# Output: [1, 3, 9]


# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dic, res = collections.defaultdict(list), []
        def inorder(node, level, dic):
            if not node: return
            inorder(node.left, level+1, dic)
            dic[level].append(node.val)
            inorder(node.right, level+1, dic)
        inorder(root, 0, dic)
        for key in sorted(dic.keys()):
            res.append(max(dic[key]))
        return res        
            

if __name__ == '__main__':
    sol = Solution()
    """
    #           1
    #          / \
    #         3   2
    #        / \   \  
    #       5   3   9 
    """
    root  = TreeNode(1)
    node1 = TreeNode(3)
    node2 = TreeNode(2)
    node3 = TreeNode(5)
    node4 = TreeNode(3)
    node5 = TreeNode(9)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.right = node5
    assert (sol.largestValues(root) == [1, 3, 9])