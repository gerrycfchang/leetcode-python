from unittest import TestCase
import unittest
import sys
sys.path.append('../')
from leetCodeUtil import TreeNode
from leetCodeUtil import BreathFirstSearch
from convert_sorted_array_binarytree import Solution


class TestSolution(TestCase):
    def test_convertCase1(self):
        ## Test case 1
        sol = Solution()
        node = sol.sortedArrayToBST([1, 2, 3])

        bfs = BreathFirstSearch()
        result1 = list(bfs.bfs(node))

        exp1 = [2, 1, 3]
        self.assertListEqual(result1, exp1)

    def test_convertCase2(self):
        ## Test case 1
        sol = Solution()
        node = sol.sortedArrayToBST([-10, -3, 0, 5, 9])

        bfs = BreathFirstSearch()
        result1 = list(bfs.bfs(node))

        exp1 = [0, -3, 9, -10, 5]
        self.assertListEqual(result1, exp1)



if __name__ == '__main__':
    unittest.main()