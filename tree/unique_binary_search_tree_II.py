# 95. Unique Binary Search Trees II
# 
# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.
# 
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3# 

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def trees(first, last):
            if first == last:
                return None
            result = []
            for root in range(first, last):
                for l in trees(first, root) or [None]:
                    for r in trees(root+1, last) or [None]:
                        node = TreeNode(root)
                        node.left, node.right  = l, r
                        result.append(node)
            return result

        return trees(1,n+1) if n > 0 else [] 

if __name__ == '__main__':
    sol = Solution()
    sol.generateTrees(0) == []