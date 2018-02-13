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

    def test_kthSmallestBinTreeCase5(self):
        sol = Solution()
        """
                Given binary tree [2, 1],

                    2
                   / \
                  1   8
                     / \
                    6   12
                """

        root = TreeNode(2)
        node1 = TreeNode(1)
        node2 = TreeNode(8)
        node3 = TreeNode(6)
        node4 = TreeNode(12)
        root.left = node1
        root.right = node2
        node2.left = node3
        node2.right = node4

        self.assertEqual(sol.kthSmallest(root, 3), 6)

if __name__ == '__main__':
    unittest.main()