from unittest import TestCase
from remove_linked_list_element import Solution
from leetCodeUtil import LinkedList
from leetCodeUtil import ListNode
import unittest

class TestSolution(TestCase):
    def test_removeLinkedListElement1(self):
        sol = Solution()

        ### Test case 1 ==> 1 > 2 > 6 > 3 > 4 > 5 > 6
        l1 = LinkedList()
        l1.insertNode(1)
        l1.insertNode(2)
        l1.insertNode(6)
        l1.insertNode(3)
        l1.insertNode(4)
        l1.insertNode(5)
        l1.insertNode(6)

        exp = LinkedList()  ## 1 > 2 > 3 > 4 > 5
        exp.insertNode(1)
        exp.insertNode(2)
        exp.insertNode(3)
        exp.insertNode(4)
        exp.insertNode(5)

        result = LinkedList()
        result.head = sol.removeElemetFromLinkedList(l1.head, 6)
        self.assertListEqual(list(result), list(exp))

    def test_removeLinkedListElement2(self):
        sol = Solution()
        ### Test case 2   ==> 1
        l2 = LinkedList()
        l2.insertNode(1)

        exp2 = LinkedList()

        result1 = LinkedList()
        result1.head = sol.removeElemetFromLinkedList(l2.head, 1)
        self.assertListEqual(list(result1), list(exp2))

        ### Test case 3   ==> 1 > 1
        l3 = LinkedList()
        l3.insertNode(1)
        l3.insertNode(1)

        exp3 = LinkedList()

        result3 = LinkedList()
        result3.head = sol.removeElemetFromLinkedList(l3.head, 1)
        self.assertListEqual(list(result3), list(exp3))

    def test_removeLinkedListElement3(self):
        sol = Solution()
        ### Test case 3   ==> 1 > 2 > 2 > 1
        l4 = LinkedList()
        l4.insertNode(1)
        l4.insertNode(2)
        l4.insertNode(2)
        l4.insertNode(1)

        exp4 = LinkedList()
        exp4.insertNode(1)
        exp4.insertNode(1)

        result4 = LinkedList()
        result4.head = sol.removeElemetFromLinkedList(l4.head, 2)
        self.assertListEqual(list(result4), list(exp4))

if __name__ == '__main__':
    unittest.main()
