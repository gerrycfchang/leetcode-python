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

class TreeNode(object):
    def __init__(self, x):
        self.left = None
        self.right = None
        self.value = x
        self.array = []

    def iterNodes(self, x):

        if x.left is not None:
            self.iterNodes(x.left)

        self.array.append(x.value)

        if x.right is not None:
            self.iterNodes(x.right)


    def __iter__(self):
        self.iterNodes(self)
        for i in range(len(self.array)):
            yield self.array[i]
