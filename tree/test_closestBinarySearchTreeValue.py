from unittest import TestCase
import unittest
import sys
sys.path.append('../')
from leetCodeUtil import TreeNode
from closest_binary_search_tree_value import Solution

class TestSolution(TestCase):
    def test_closestBinarySearchTreeValueCase1(self):
        ### Test case 1
        """

            19
           / \
          7  20
         /  \
        5   18
        """
        root = TreeNode(19)
        node1 = TreeNode(7)
        node2 = TreeNode(20)
        node3 = TreeNode(5)
        node4 = TreeNode(18)

        root.left = node1
        root.right = node2
        node1.left = node3
        node1.right = node4
        sol = Solution()
        result = sol.closestValue(root, 8)


        self.assertEqual(result, 7)

    def test_closestBinarySearchTreeValueCase2(self):
        ### Test case 1
        """

            35
           / \
          7  100
         /  \
        5   18
        """
        root = TreeNode(35)
        node1 = TreeNode(7)
        node2 = TreeNode(100)
        node3 = TreeNode(5)
        node4 = TreeNode(18)

        root.left = node1
        root.right = node2
        node1.left = node3
        node1.right = node4
        sol = Solution()
        result = sol.closestValue(root, 97)


        self.assertEqual(result, 100)

if __name__ == '__main__':
    unittest.main()