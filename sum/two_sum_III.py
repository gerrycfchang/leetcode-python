# Design and implement a TwoSum class. It should support the following operations: add and find.
# 
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
# 
# For example,
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false

class TwoSum(object):
    def __init__(self):
        """
        initialize your data structure here
        """
        self.table = {}

    
    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number not in self.table:
            self.table[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """

        for key in self.table.keys():
            target = value - key
            if (target) in self.table:
                return True
        return False

if __name__ == '__main__':
    sol = TwoSum()

    for i in (1, 3, 5):
        sol.add(i)

    assert sol.find(4) == True
    assert sol.find(7) == False

    