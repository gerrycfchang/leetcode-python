from unittest import TestCase
import unittest
from course_schedule import Solution

class TestSolution(TestCase):
    def test_courseScheduleCase1(self):
        sol = Solution()
        courses = [[1,0]]

        self.assertEqual(sol.canFinish(2, courses), True)

    def test_courseScheduleCase2(self):
        sol = Solution()
        courses = [[0, 1]]

        self.assertEqual(sol.canFinish(2, courses), True)

    def test_courseScheduleCase3(self):
        sol = Solution()
        courses = [[1, 0],[0, 1]]

        self.assertEqual(sol.canFinish(2, courses), False)

    def test_courseScheduleCase4(self):
        sol = Solution()
        courses = [[1, 0],[0, 4],[4, 3], [3, 2], [4, 2]]

        self.assertEqual(sol.canFinish(5, courses), True)

if __name__ == '__main__':
    unittest.main()