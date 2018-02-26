"""
Given a Binary Search Tree and a target number, return true 
if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True


"""
import sys
sys.path.append('../')
from leetCodeUtil import TreeNode

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def dfs(node, k, dict):
            if not node: return False
            target = k - node.value
            if target in dict:
                return True
            else:
                dict[node.value] = 1
                return dfs(node.left, k, dict) or dfs(node.right, k, dict)
        if not root: return False
        dict = {}
        return dfs(root, k, dict)
        
if __name__ == '__main__':
    sol = Solution()
    sol = Solution()

    root = TreeNode(5)
    node2 = TreeNode(2)
    node3 = TreeNode(7)

    root.left = node2
    root.right = node3

    assert sol.findTarget(root, 9) == True

