from unittest import TestCase
import unittest
import sys
sys.path.append('../')
from leetCodeUtil import TreeNode
from longest_univalue_path import Solution

class TestSolution(TestCase):
    def test_LongestUnivalueCase1(self):
        """
                    5
                   / \
                  4   5
                 / \ / \
                1  1    5

        """

        node = TreeNode(5)

        leftNode = TreeNode(4)
        rightNode = TreeNode(5)
        node.left = leftNode
        node.right = rightNode

        thirdLevelLeftNode1 = TreeNode(1)
        thirdLevelLeftNode2 = TreeNode(1)
        thirdLevelRightNode1 = TreeNode(5)

        leftNode.left = thirdLevelLeftNode1
        leftNode.right = thirdLevelLeftNode2
        rightNode.right = thirdLevelRightNode1

        sol = Solution()
        self.assertEqual(sol.longestUnivaluePath(node), 2)


    def test_LongestUnivalueCase2(self):
        """
                    1
                   / \
                  4   5
                 / \ / \
                4  4    5

        """

        node = TreeNode(1)

        leftNode = TreeNode(4)
        rightNode = TreeNode(5)
        node.left = leftNode
        node.right = rightNode

        thirdLevelLeftNode1 = TreeNode(4)
        thirdLevelLeftNode2 = TreeNode(4)
        thirdLevelRightNode1 = TreeNode(5)

        leftNode.left = thirdLevelLeftNode1
        leftNode.right = thirdLevelLeftNode2
        rightNode.right = thirdLevelRightNode1

        sol = Solution()
        self.assertEqual(sol.longestUnivaluePath(node), 2)



if __name__ == '__main__':
    unittest.main()