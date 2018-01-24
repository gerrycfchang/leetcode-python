from unittest import TestCase
import unittest
from valid_parentheses import Solution

class TestSolution(TestCase):
    def test_validParentheses(self):
        sol = Solution()
        self.assertEqual(sol.isValid('()(())'),True)
        self.assertEqual(sol.isValid('(){}[]'), True)
        self.assertEqual(sol.isValid('(]'), False)
        self.assertEqual(sol.isValid(''), False)
        self.assertEqual(sol.isValid('((({})[]){})'), True)
        self.assertEqual(sol.isValid(']'), False)

if __name__ == '__main__':
    unittest.main()
