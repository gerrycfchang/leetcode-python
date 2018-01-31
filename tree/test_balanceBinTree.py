from unittest import TestCase
import unittest
import sys
sys.path.append('../')
from leetCodeUtil import TreeNode
from balance_bin_tree import Solution

class TestSolution(TestCase):
    def test_balanceBinTreeCase1(self):
        sol = Solution()

        ### Test case 1
        """
        Given binary tree [3,9,20,null,null,15,7],

            1
             \
              2
               \
                3
        """
        root  = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)

        root.right = node1
        node1.right = node2

        self.assertEqual(sol.isBalanced(root), False)

    def test_balanceBinTreeCase2(self):
        sol = Solution()

        ### Test case 1
        """
        Given binary tree [1,2,2,3,null,null,3,4,null,null,4],

            1
           / \
          2   2
         /     \
        3       3
       /         \
      4           4
        """
        root  = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(3)
        node5 = TreeNode(4)
        node6 = TreeNode(4)

        root.left = node1
        root.right = node2
        node1.left = node3
        node2.right = node4
        node3.left = node5
        node4.right = node6

        self.assertEqual(sol.isBalanced(root), False)

if __name__ == '__main__':
    unittest.main()