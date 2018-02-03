from unittest import TestCase
import unittest
from decode_string import Solution


class TestSolution(TestCase):
    def test_decompressStringCase1(self):
        sol = Solution()

        self.assertEqual(sol.decompress('a3[b2[c1[d]]]e'), 'abcdcdbcdcdbcdcde')

    def test_decompressStringCase2(self):
        sol = Solution()

        self.assertEqual(sol.decompress('3[a]2[bc]'), 'aaabcbc')

    def test_decompressStringCase3(self):
        sol = Solution()

        self.assertEqual(sol.decompress('3[a2[c]]'), 'accaccacc')

    def test_decompressStringCase4(self):
        sol = Solution()

        self.assertEqual(sol.decompress('2[abc]3[cd]ef'), 'abcabccdcdcdef')

    def test_decompressStringCase5(self):
        sol = Solution()

        self.assertEqual(sol.decompress('abcdef'), 'abcdef')

    def test_decompressStringCase6(self):
        sol = Solution()

        self.assertEqual(sol.decompress('10[ab]'), 'abababababababababab')


if __name__ == '__main__':
    unittest.main()