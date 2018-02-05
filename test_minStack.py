from unittest import TestCase
import unittest
from min_stack import MinStack

class TestSolution(TestCase):
    def test_minStackCase1(self):

        obj = MinStack()
        obj.push(-2)
        obj.push(0)
        obj.push(-3)
        param_1 = obj.getMin()
        obj.pop()
        param_2 = obj.top()
        param_3 = obj.getMin()

        self.assertEqual(param_1, -3)
        self.assertEqual(param_2, 0)
        self.assertEqual(param_3, -2)

    def test_minStackCase2(self):

        obj = MinStack()
        obj.push(-1)
        param_1 = obj.top()
        param_2 = obj.getMin()

        self.assertEqual(param_1, -1)
        self.assertEqual(param_2, -1)

    def test_minStackCase3(self):

        obj = MinStack()
        obj.push(2)
        obj.push(0)
        obj.push(3)
        obj.push(0)

        param_1 = obj.getMin()
        obj.pop()
        param_3 = obj.getMin()
        obj.pop()
        param_5 = obj.getMin()
        obj.pop()
        param_7 = obj.getMin()

        self.assertEqual(param_1, 0)

        self.assertEqual(param_3, 0)

        self.assertEqual(param_5, 0)

        self.assertEqual(param_7, 2)


if __name__ == '__main__':
    unittest.main()