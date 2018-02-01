from unittest import TestCase
import unittest
import sys
sys.path.append('../')
from leetCodeUtil import LinkedList
from leetCodeUtil import ListNode
from intersection_two_lists import Solution

class TestSolution(TestCase):
    def test_intersectionTwoLinkedListsCase1(self):
        sol = Solution()
        """
        A:          a1 > a2
                             >
                                c1 > c2 > c3
                             >
        B:     b1 > b2 > b3

        """

        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        node6 = ListNode(6)
        node7 = ListNode(7)
        node8 = ListNode(8)
        node6.next = node7
        node7.next = node8
        node8.next = node3


        pcross = sol.getIntersectionNode(node1, node6)
        self.assertEqual(pcross.val, 3)


    def test_intersectionTwoLinkedListsCase2(self):
        sol = Solution()
        """
        A:          a1 > a2

        B:     b1 > b2 > b3

        """

        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2


        node6 = ListNode(6)
        node7 = ListNode(7)
        node8 = ListNode(8)
        node6.next = node7
        node7.next = node8


        pcross = sol.getIntersectionNode(node1, node6)
        self.assertEqual(pcross, None)

if __name__ == '__main__':
    unittest.main()

