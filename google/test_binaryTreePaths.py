from unittest import TestCase
import unittest
import sys
sys.path.append('../')
from leetCodeUtil import TreeNode
from binary_tree_paths import Solution

class TestSolution(TestCase):
    def test_binaryTreePathsCase1(self):
        ### Test case 1
        """
        Given binary tree [3,9,20,null,null,15,7],

            1
           / \
          2   3
            \
            5
        """
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(5)

        root.left = node1
        root.right = node2
        node1.right = node3
        sol = Solution()
        result = sol.binaryTreePaths(root)
        exp = ["1->2->5", "1->3"]

        result.sort()
        exp.sort()
        self.assertListEqual(result, exp)

    def test_binaryTreePathsCase2(self):
        root = None

        sol = Solution()
        result = sol.binaryTreePaths(root)
        self.assertListEqual(result, [])


### Test case 1

if __name__ == '__main__':
    unittest.main()