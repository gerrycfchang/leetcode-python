"""
Put some common classes here
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNode(self, x):
        node = ListNode(x)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = self.head

        else:
            self.tail.next = node
            self.tail = node

    def __iter__(self):
        item = ListNode(-1)
        item = self.head
        while item is not None:
            yield item.val
            item = item.next

