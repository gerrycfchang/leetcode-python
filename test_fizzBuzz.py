from unittest import TestCase
import unittest
from fizz_buzz import Solution

class TestSolution(TestCase):
    def test_fizzBuzzCase1(self):
        sol = Solution()

        exp = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz"
        ]

        self.assertListEqual(sol.fizzBuzz(15), exp)

    def test_fizzBuzzCase2(self):
        sol = Solution()

        exp = [
            "1",
            "2",
            "Fizz",
        ]

        self.assertListEqual(sol.fizzBuzz(3), exp)




if __name__ == "__main__":
    unittest.main()