from unittest import TestCase
import unittest
from leetCodeUtil import TreeNode
from invert_binary_tree import Solution

class TestSolution(TestCase):
    def test_invertBinaryTreeCase1(self):

        sol = Solution()

        ## Test case 1
        node = TreeNode(2)
        leftNode = TreeNode(1)
        rightNode = TreeNode(3)

        node.left = leftNode
        node.right = rightNode

        result1 = list((sol.invertTree(node)).getDFS(node))
        exp1 = [3, 2, 1]
        self.assertListEqual(result1, exp1)

    def test_invertBinaryTreeCase2(self):
        sol = Solution()
        ## Test case 1

        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node6 = TreeNode(6)
        node7 = TreeNode(7)
        node9 = TreeNode(9)

        node4.left = node2
        node4.right = node7
        node2.left = node1
        node2.right = node3
        node7.left = node6
        node7.right = node9

        result = list((sol.invertTree(node4)).getDFS(node4))
        exp = [9, 7, 6, 4, 3, 2, 1]
        self.assertListEqual(result, exp)

if __name__ == '__main__':
    unittest.main()
