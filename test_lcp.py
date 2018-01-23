from unittest import TestCase
from LCP import LCPSolution
import unittest

class TestSolution(TestCase):
    def test_(self):
        sol = LCPSolution()
        self.assertEqual(sol.longestCommonPrefix(['abc', 'abcde', 'abbbb', 'abcd']), 'ab')
        self.assertEqual(sol.longestCommonPrefix(['abcde', 'cbbbb', 'bvcd']), '')
        self.assertEqual(sol.longestCommonPrefix(['abcde', 'abbbb', 'avcd']), 'a')
        self.assertEqual(sol.longestCommonPrefix([]), '')
        self.assertEqual(sol.longestCommonPrefix(['a']), 'a')
        self.assertEqual(sol.longestCommonPrefix(['aa', 'a']), 'a')
        self.assertEqual(sol.longestCommonPrefix(["abab","aba",""]), '')


if __name__ == '__main__':
    unittest.main()
