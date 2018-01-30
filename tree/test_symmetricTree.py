from unittest import TestCase
import unittest
from symmetric_tree import Solution
import sys
sys.path.append('../')
from leetCodeUtil import TreeNode


class TestSolution(TestCase):
    def test_symmetricTreeCase1(self):
        ## Test case 1
        """
            1
           / \
          2   2
         / \ / \
        3  4 4  3

        """
        node = TreeNode(1)
        leftNode = TreeNode(2)
        rightNode = TreeNode(2)

        node.left = leftNode
        node.right = rightNode

        sol = Solution()
        self.assertEqual(sol.isSymmetric(node), True)


    def test_symmetricTreeCase2(self):
        ## Test case 2
        """
            1
           / \
          2   2
         / \ / \
           3    3

        """
        node = TreeNode(1)

        leftNode = TreeNode(2)
        rightNode = TreeNode(2)
        node.left = leftNode
        node.right = rightNode

        thirdLevelRightNode1 = TreeNode(3)
        thirdLevelRightNode2 = TreeNode(3)

        leftNode.right = thirdLevelRightNode1
        rightNode.right = thirdLevelRightNode2

        sol = Solution()
        self.assertEqual(sol.isSymmetric(node), False)


    def test_symmetricTreeCase3(self):
        ## Test case 2
        """
            1
           / \
          2   2
         / \ / \
        3  4    3

        """

        node = TreeNode(1)

        leftNode = TreeNode(2)
        rightNode = TreeNode(2)
        node.left = leftNode
        node.right = rightNode

        thirdLevelLeftNode1 = TreeNode(3)
        thirdLevelLeftNode2 = TreeNode(4)
        thirdLevelRightNode1 = TreeNode(3)

        leftNode.left = thirdLevelLeftNode1
        leftNode.right = thirdLevelLeftNode2
        rightNode.right = thirdLevelRightNode1


        sol = Solution()
        self.assertEqual(sol.isSymmetric(node), False)



if __name__ == '__main__':
    unittest.main()