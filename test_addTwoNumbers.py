from unittest import TestCase
from add_two_numbers import Solution
from leetCodeUtil import LinkedList
import unittest

class TestSolution(TestCase):
    def test_addTwoNumbersCase1(self):
        sol = Solution()

        l1 = LinkedList()
        l1.insertNode(2)
        l1.insertNode(4)
        l1.insertNode(3)

        l2 = LinkedList()
        l2.insertNode(5)
        l2.insertNode(6)
        l2.insertNode(4)

        exp = LinkedList()
        exp.insertNode(7)
        exp.insertNode(0)
        exp.insertNode(8)

        result = LinkedList()
        result.head = (sol.addTwoNumbers(l1.head,l2.head))
        self.assertListEqual(list(result),list(exp))

    def test_addTwoNumbersCase2(self):
        sol = Solution()

        l1 = LinkedList()
        l1.insertNode(2)
        l1.insertNode(4)
        l1.insertNode(3)

        l2 = LinkedList()
        l2.insertNode(5)
        l2.insertNode(6)


        exp = LinkedList()
        exp.insertNode(7)
        exp.insertNode(0)
        exp.insertNode(4)

        result = LinkedList()
        result.head = (sol.addTwoNumbers(l1.head,l2.head))
        self.assertListEqual(list(result),list(exp))

    def test_addTwoNumbersCase3(self):
        sol = Solution()

        l1 = LinkedList()
        l1.insertNode(2)
        l1.insertNode(4)
        l1.insertNode(3)

        l2 = LinkedList()


        exp = LinkedList()
        exp.insertNode(2)
        exp.insertNode(4)
        exp.insertNode(3)

        result = LinkedList()
        result.head = (sol.addTwoNumbers(l1.head,l2.head))
        self.assertListEqual(list(result),list(exp))

    def test_addTwoNumbersCase4(self):
        sol = Solution()

        l1 = LinkedList()
        l1.insertNode(9)

        l2 = LinkedList()
        l2.insertNode(9)


        exp = LinkedList()
        exp.insertNode(8)
        exp.insertNode(1)

        result = LinkedList()
        result.head = (sol.addTwoNumbers(l1.head,l2.head))
        self.assertListEqual(list(result),list(exp))

    def test_addTwoNumbersCase5(self):
        sol = Solution()

        l1 = LinkedList()
        l1.insertNode(1)

        l2 = LinkedList()
        l2.insertNode(9)
        l2.insertNode(9)


        exp = LinkedList()
        exp.insertNode(0)
        exp.insertNode(0)
        exp.insertNode(1)

        result = LinkedList()
        result.head = (sol.addTwoNumbers(l1.head,l2.head))
        self.assertListEqual(list(result),list(exp))

if __name__ == '__main__':
    unittest.main()