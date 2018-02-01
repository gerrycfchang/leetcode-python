from unittest import TestCase
import unittest
from excel_sheet_column import Solution


class TestSolution(TestCase):
    def test_excelSheetColumnCase1(self):

        sol = Solution()
        self.assertEqual(sol.convertToTitle(1), 'A')

    def test_excelSheetColumnCase2(self):
        sol = Solution()
        self.assertEqual(sol.convertToTitle(27), 'AA')

    def test_excelSheetColumnCase3(self):
        sol = Solution()
        self.assertEqual(sol.convertToTitle(512), 'SR')


if __name__ == '__main__':
    unittest.main()