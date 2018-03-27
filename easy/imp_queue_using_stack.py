# 232. Implement Queue using Stacks
# 
# Implement the following operations of a queue using stacks.
# 
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.queue.pop(0)        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue[0]        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.queue) == 0        


# Your MyQueue object will be instantiated and called as such:

if __name__ == '__main__':

    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()

    assert param_2 == 1
    assert param_3 == 2
    assert param_4 == False