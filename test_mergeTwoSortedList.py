from unittest import TestCase
from merge_two_sorted_list import MergeTwoSortedList
from leetCodeUtil import LinkedList
import unittest

class TestSolution(TestCase):
    def test_mergetwosortedlist(self):
        sol = MergeTwoSortedList()

        l1 = LinkedList()
        l1.insertNode(1)
        l1.insertNode(2)
        l1.insertNode(3)

        l2 = LinkedList()
        l2.insertNode(3)
        l2.insertNode(4)

        exp = LinkedList()
        exp.insertNode(1)
        exp.insertNode(2)
        exp.insertNode(3)
        exp.insertNode(3)
        exp.insertNode(4)

        result = LinkedList()
        result.head = sol.mergeTwoLists(l1.head,l2.head)
        self.assertListEqual(list(result),list(exp))

if __name__ == '__main__':
    unittest.main()