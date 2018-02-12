from unittest import TestCase
import unittest
from course_schedule_II import Solution

class TestSolution(TestCase):
    def test_courseScheduleIICase1(self):
        sol = Solution()
        courses = [[1,0]]

        self.assertListEqual(sol.findOrder(2, courses), [0, 1])

    def test_courseScheduleIICase2(self):
        sol = Solution()
        courses = [[1,0],[2,0],[3,1],[3,2]]

        self.assertListEqual(sol.findOrder(4, courses), [0,2,1,3])


if __name__ == '__main__':
    unittest.main()