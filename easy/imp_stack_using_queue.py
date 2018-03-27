# 225. Implement Stack using Queues
# 
# Implement the following operations of a stack using queues.
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.pop()        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[-1]        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.stack) == 0        


# Your MyStack object will be instantiated and called as such:
if __name__ == '__main__':

    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()

    assert param_2 == 4
    assert param_3 == 3
    assert param_4 == False