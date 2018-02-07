from unittest import TestCase
import unittest
from unique_word_abbreviation import ValidWordAbbr

class TestSolution(TestCase):
    def test_uniqueWordAbbrCase1(self):
        dictionary = ["deer", "door", "cake", "card"]
        vwa = ValidWordAbbr(dictionary)
        self.assertEqual(vwa.isUnique("dear"), False)
        self.assertEqual(vwa.isUnique("cart"), True)
        self.assertEqual(vwa.isUnique("cane"), False)
        self.assertEqual(vwa.isUnique("make"), True)

    def test_uniqueWordAbbrCase2(self):
        dictionary = ["door", "door"]
        vwa = ValidWordAbbr(dictionary)
        self.assertEqual(vwa.isUnique("door"), True)

    def test_uniqueWordAbbrCase3(self):
        dictionary = ["dear", "door"]
        vwa = ValidWordAbbr(dictionary)
        self.assertEqual(vwa.isUnique("door"), False)


if __name__ == '__main__':
    unittest.main()