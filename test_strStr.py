from unittest import TestCase
import unittest
from strStr import Solution

class TestSolution(TestCase):
    def test_case1(self):
        sol = Solution()
        hstr = 'hello'
        str = 'll'

        self.assertEqual(sol.strStr(hstr,str), 2)

    def test_case2(self):
        sol = Solution()
        hstr = 'aaaaa'
        str = 'bba'

        self.assertEqual(sol.strStr(hstr,str), -1)

    def test_case3(self):
        sol = Solution()
        hstr = ''
        str = 'bba'

        self.assertEqual(sol.strStr(hstr,str), -1)

    def test_case4(self):
        sol = Solution()
        hstr = ''
        str = ''

        self.assertEqual(sol.strStr(hstr,str), 0)

    def test_case5(self):
        sol = Solution()
        hstr = 'a'
        str = 'a'

        self.assertEqual(sol.strStr(hstr,str), 0)

if __name__ == '__main__':
    unittest.main()