from unittest import TestCase
from palindrome_linked_list import Solution
import sys
sys.path.append('../')
from leetCodeUtil import LinkedList
from leetCodeUtil import ListNode
import unittest

class TestSolution(TestCase):
    def test_palindromeCase1(self):
        sol = Solution()

        l1 = LinkedList()
        l1.insertNode(1)
        l1.insertNode(2)
        l1.insertNode(3)
        l1.insertNode(4)
        l1.insertNode(3)
        l1.insertNode(2)
        l1.insertNode(1)

        self.assertEqual(sol.isPalindrome(l1.head), True)

    def test_palindromeCase2(self):
        sol = Solution()

        l2 = LinkedList()
        l2.insertNode(1)
        l2.insertNode(2)

        self.assertEqual(sol.isPalindrome(l2.head), False)

    def test_palindromeCase3(self):
        sol = Solution()

        l3 = LinkedList()

        self.assertEqual(sol.isPalindrome(l3.head), True)


if __name__ == '__main__':
    unittest.main()
