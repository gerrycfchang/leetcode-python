from unittest import TestCase
import sys
sys.path.append('../')
from leetCodeUtil import LinkedList
from leetCodeUtil import ListNode
import unittest
from linked_list_cycle_II import Solution

class TestSolution(TestCase):
    def test_linkedListCycleIICase1(self):
        sol = Solution()

        l1 = LinkedList()
        l1.insertNode(1)

        node = sol.hasCycle(l1.head)

        self.assertEqual(node, None)


    def test_linkedListCycleIICase2(self):
        sol = Solution()

        """
        1 > 2 > 3 > 4 > 5 > 6 > 5

        """

        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        node6 = ListNode(6)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6
        node6.next = node5

        node = sol.hasCycle(node1)

        self.assertEqual(node.val, 5)

    def test_linkedListCycleIICase3(self):
        sol = Solution()

        """
        1 > 2 > 3 > 4 > 5 > 6 > 5

        """

        node1 = ListNode(3)
        node2 = ListNode(2)
        node3 = ListNode(0)
        node4 = ListNode(-4)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2

        node = sol.hasCycle(node1)

        self.assertEqual(node.val, 2)

if __name__ == '__main__':
    unittest.main()