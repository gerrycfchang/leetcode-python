"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class LinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None

    def insertNode(self, value):
        if self.first is None and self.last is None:
            self.first = ListNode(value)
            self.last = self.first
        else:
            item = ListNode(-1)
            item.val = value
            self.last.next = item
            self.last = item

    def __iter__(self):
        item = ListNode(-1)
        item = self.first
        result = []
        while item is not None:
            result.append(item.val)
            yield item.val
            item = item.next
        #return result

class MergeTwoSortedList(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prehead = ListNode(-1)
        point = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        if l1 is not None:
            point.next = l1
        elif l2 is not None:
            point.next = l2

        return prehead.next