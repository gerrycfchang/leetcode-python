
from unittest import TestCase
import unittest
import sys
sys.path.append('../')
from leetCodeUtil import TreeNode
from leetCodeUtil import ListNode
from convert_sorted_list_binarytree import Solution


class TestSolution(TestCase):
    def test_convertCase1(self):
        ## Test case 1
        sol = Solution()
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        root = sol.sortedListToBST(node1)
        result = list(root.getBFS(root))

        exp1 = [3, 1, 4, 2, 5]
        self.assertListEqual(result, exp1)



if __name__ == '__main__':
    unittest.main()