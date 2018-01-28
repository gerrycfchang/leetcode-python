from unittest import TestCase
import unittest
import sys
from insert_node_binarytree import Solution
sys.path.append('../')
from leetCodeUtil import BreathFirstSearch
from leetCodeUtil import TreeNode


class TestSolution(TestCase):
    def test_insertNodeCase1(self):
        root = TreeNode(5)

        sol = Solution()
        sol.insertBinaryTreeNode(root, 3)
        sol.insertBinaryTreeNode(root, 7)
        sol.insertBinaryTreeNode(root, 1)
        sol.insertBinaryTreeNode(root, 6)
        sol.insertBinaryTreeNode(root, 9)

        bfs = BreathFirstSearch()
        result1 = list(bfs.bfs(root))

        exp1 = [5, 3, 7, 1, 6, 9]
        self.assertListEqual(result1, exp1)
if __name__ == '__main__':
    unittest.main()