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
        self.queue = []

    def getDFS(self, x):

        if x.left is not None:
            self.getDFS(x.left)

        self.array.append(x.value)

        if x.right is not None:
            self.getDFS(x.right)

        return self.array

    def getBFS(self, x):
        self.array.append(x.value)
        if x.left is not None:
            self.queue.append(x.left)
        if x.right is not None:
            self.queue.append(x.right)

        if (len(self.queue) > 0):
            self.getBFS(self.queue.pop(0))
        else:
            return

        return self.array

    def __iter__(self):
        for i in range(len(self.array)):
            yield self.array[i]




