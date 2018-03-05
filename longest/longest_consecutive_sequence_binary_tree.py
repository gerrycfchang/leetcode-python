
"""
Given a binary tree, find the length of the longest consecutive sequence path. 

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,

   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.

   2
    \
     3
    / 
   2    
  / 
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2
"""
import sys
sys.path.append('../')
from leetCodeUtil import TreeNode

class Solution(object):
    def longestConsecutive(self, root):
        Solution.ret = 0
        self.dfs(root, root.value, 0)
        return Solution.ret

    def dfs(self, node, value, out):
        if not node: return
        if node.value == value + 1:
            out +=1
        else:
            out = 1
        Solution.ret = max (Solution.ret, out)
        self.dfs(node.left, node.value, out)
        self.dfs(node.right, node.value, out)



if __name__ == '__main__':
    sol = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.right = node3
    node3.left  = node2
    node3.right = node4
    node4.right = node5
    assert sol.longestConsecutive(node1) == 3


    sample2 = TreeNode(2)
    sample3 = TreeNode(3)
    sample4 = TreeNode(2)
    sample5 = TreeNode(1)
    sample2.right = sample3
    sample3.left = sample4
    sample4.left = sample5
    assert sol.longestConsecutive(sample2) == 2


