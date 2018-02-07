from unittest import TestCase
import unittest
from add_strings import Solution

class TestSolution(TestCase):
    def test_addStringsCase1(self):
        sol = Solution()
        self.assertEqual(sol.addStrings('0','0'),'0')

    def test_addStringsCase2(self):
        sol = Solution()
        self.assertEqual(sol.addStrings('1', '9'), '10')



if __name__ == '__main__':
    unittest.main()