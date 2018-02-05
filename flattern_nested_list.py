"""
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
    def __init__(self, x):
        self.nestedInt = x


    def append(self, item):
        self.nestedInt.append(item)

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

        if type(self.nestedInt) == int:
            return True
        else:
            return False

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if type(self.nestedInt) == int:
            return self.nestedInt
#
    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        if type(self.nestedInt) == list:
            return self.nestedInt

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.result = []
        self.index = -1
        self.getItemFromList(nestedList)
        # for i in range (len(self.result)):
        #    nestedList.insert(i, self.result[i])

    def getItemFromList(self, itemList):
        if itemList is None:
            return

        while(itemList is not None):
            if type(itemList) == list and len(itemList) > 0:
                item = itemList.pop(0)
            #elif len(itemList) > 0:
            #    item = itemList
            else:
                return

            if item.isInteger() == True:
                self.result.append(item)
            else:
                self.getItemFromList(item.getList())

    def next(self):
        """
        :rtype: int
        """
        return self.result.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.result) > 0:
            return True
        else:
            return False

