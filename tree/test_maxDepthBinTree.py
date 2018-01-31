from unittest import TestCase
import unittest
import sys
sys.path.append('../')
from leetCodeUtil import TreeNode
from max_depth_bin_tree import Solution

class TestSolution(TestCase):
    def test_maxDepthBinTreeCase1(self):
        sol = Solution()

        ### Test case 1
        """
        Given binary tree [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
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

        self.assertEqual(sol.maxDepth(root), 3)

if __name__ == '__main__':
    unittest.main()