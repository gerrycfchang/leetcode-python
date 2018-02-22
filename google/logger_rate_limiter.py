"""
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.
"""
class Logger(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.logger = defaultdict(set)

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.logger:
            self.logger[message] = timestamp
            return True
        else:
            if timestamp - self.logger[message] < 10:
                return False
            else:
                self.logger[message] = timestamp
                return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

if __name__ == '__main__':
    logger = Logger()

    result = logger.shouldPrintMessage(1, "foo")
    assert result == True

    result = logger.shouldPrintMessage(2, "bar")
    assert result == True

    result = logger.shouldPrintMessage(3, "foo")
    assert result == False

    result = logger.shouldPrintMessage(8, "bar")
    assert result == False

    result = logger.shouldPrintMessage(10, "foo")
    assert result == False

    result = logger.shouldPrintMessage(11, "foo")
    assert result == True

