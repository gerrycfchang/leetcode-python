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
