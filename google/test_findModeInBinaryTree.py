from unittest import TestCase
import unittest
import sys
sys.path.append('../')
from leetCodeUtil import TreeNode
from find_mode_in_binary_tree import Solution

class TestSolution(TestCase):
    def test_findModeInBSTCase1(self):
        ### Test case 1
        """
        Given BST [1,null,2,2],
           1
            \
             2
            /
           2

        """
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(2)


        root.right = node1
        node1.left = node2
        sol = Solution()
        
        self.assertListEqual(sol.findMode(root), [2])

if __name__ == '__main__':
    unittest.main()
