"""

"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) >= 1:
            index = len(self.stack) - 1
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) >= 1:
            result = self.stack[len(self.stack)-1]
            return result
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) >= 1:
            self.min = min(self.stack)
        else:
            self.min = None

        return self.min

if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    param_1 = obj.getMin()
    obj.pop()
    param_2 = obj.top()
    param_3 = obj.getMin()
    assert (param_1 == -3)
    assert (param_2 ==  0)
    assert (param_3 == -2)

    obj1 = MinStack()
    obj1.push(-1)
    param_1 = obj1.top()
    param_2 = obj1.getMin()
    assert (param_1 == -1)
    assert (param_2 == -1)

    obj2 = MinStack()
    obj2.push(2)
    obj2.push(0)
    obj2.push(3)
    obj2.push(0)
    param_1 = obj2.getMin()
    obj2.pop()
    param_3 = obj2.getMin()
    obj2.pop()
    param_5 = obj2.getMin()
    obj2.pop()
    param_7 = obj2.getMin()
    assert (param_1 == 0)
    assert (param_3 == 0)
    assert (param_5 == 0)
    assert (param_7 == 2)
