from unittest import TestCase
import unittest
from logger_rate_limiter import Logger

class TestSolution(TestCase):
    def test_loggerRateLimiterCase1(self):
        logger = Logger()

        result = logger.shouldPrintMessage(1, "foo")
        self.assertEqual(result, True)

        result = logger.shouldPrintMessage(2, "bar")
        self.assertEqual(result, True)

        result = logger.shouldPrintMessage(3, "foo")
        self.assertEqual(result, False)


        result = logger.shouldPrintMessage(8, "bar")
        self.assertEqual(result, False)


        result = logger.shouldPrintMessage(10, "foo")
        self.assertEqual(result, False)


        result = logger.shouldPrintMessage(11, "foo")
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()