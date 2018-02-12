from unittest import TestCase
import unittest
from reverse_words_in_string import Solution

class TestSolution(TestCase):
    def test_reverseWordsInStringCase1(self):
        sol = Solution()
        inp = "the sky is blue"
        exp = 'blue is sky the'

        self.assertEqual(sol.reverseWords(inp), exp)

    def test_reverseWordsInStringCase2(self):
        sol = Solution()
        inp = " a"
        exp = 'a'

        self.assertEqual(sol.reverseWords(inp), exp)

    def test_reverseWordsInStringCase3(self):
        sol = Solution()
        inp = " "
        exp = ''

        self.assertEqual(sol.reverseWords(inp), exp)


if __name__ == '__main__':
    unittest.main()