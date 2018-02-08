from unittest import TestCase
import unittest
from group_shift_string import Solution

class TestSolution(TestCase):
    def test_groupShiftStringCase1(self):

        sol = Solution()
        str = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

        result = sol.groupStrings(str)
        result.sort()

        exp = [
          ["abc","bcd","xyz"],
          ["az","ba"],
          ["acef"],
          ["a","z"]
        ]
        exp.sort()

        self.assertListEqual(result, exp)

    def test_groupShiftStringCase2(self):

        sol = Solution()
        str = ["abc", "cbd", "a", "z"]

        result = sol.groupStrings(str)
        result.sort()

        exp = [
          ["abc"],
          ["cbd"],
          ["a","z"]
        ]
        exp.sort()

        self.assertListEqual(result, exp)


if __name__ == '__main__':
    unittest.main()