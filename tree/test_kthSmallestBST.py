from unittest import TestCase
import unittest
import sys
sys.path.append('../')
from leetCodeUtil import TreeNode
from kth_smallest_BST import Solution

class TestSolution(TestCase):
    def test_kthSmallestBinTreeCase1(self):
        sol = Solution()
        """
                Given binary tree [1, null, 2],

                    1
                     \
                      2

                """

        root = TreeNode(1)
        node1 = TreeNode(2)
        root.right = node1

        self.assertEqual(sol.kthSmallest(root, 2), 2)

    def test_kthSmallestBinTreeCase2(self):
        sol = Solution()
        """
                Given binary tree [1],

                    1

                """

        root = TreeNode(1)

        self.assertEqual(sol.kthSmallest(root, 1), 1)

    def test_kthSmallestBinTreeCase3(self):
        sol = Solution()
        """
                Given binary tree [1, null, 2],

                    1
                     \
                      2

                """

        root = TreeNode(1)
        node1 = TreeNode(2)
        root.right = node1

        self.assertEqual(sol.kthSmallest(root, 1), 1)

    def test_kthSmallestBinTreeCase4(self):
        sol = Solution()
        """
                Given binary tree [2, 1],

                    2
                   /
                  1

                """

        root = TreeNode(2)
        node1 = TreeNode(1)
        root.left = node1

        self.assertEqual(sol.kthSmallest(root, 1), 1)

if __name__ == '__main__':
    unittest.main()