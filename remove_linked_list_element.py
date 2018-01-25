"""
Remove all elements from a linked list of integers that have value val.
Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""

from leetCodeUtil import ListNode

class Solution(object):
    def removeElemetFromLinkedList(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        item = head
        while item is not None:

            if item == head:
                if item.val == val:
                    head = head.next
                    item = item.next
                    continue

            if item.next is not None and item.next.val == val:
                item.next = item.next.next
                continue

            item = item.next

        return head