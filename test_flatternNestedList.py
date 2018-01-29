from unittest import TestCase
import unittest
from flattern_nested_list import NestedIterator
from flattern_nested_list import NestedInteger

class TestSolution(TestCase):
    def test_Case1(self):
        # itemList = [[1,[1,3]],2]
        nest11 = NestedInteger(1)
        nest111 = NestedInteger(1)
        nest112 = NestedInteger(3)
        firstList = []
        firstList.append(nest111)
        firstList.append(nest112)
        firstnest = NestedInteger(firstList)

        firstList1 = []
        firstList1.append(nest11)
        firstList1.append(firstnest)


        nest1 = NestedInteger(firstList1)
        nest2 = NestedInteger(2)

        itemList = []
        itemList.append(nest1)
        itemList.append(nest2)

        i, v = NestedIterator(itemList), []
        while i.hasNext():
            v.append(i.next())

        resultArray = []
        for j in range(len(v)):
            resultArray.append(v[j].getInteger())

        exp = [1,1,3,2]

        self.assertListEqual(resultArray,exp)



if __name__ =='__main__':
    unittest.main()

