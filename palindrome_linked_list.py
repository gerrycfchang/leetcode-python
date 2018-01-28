"""
Given a singly linked list, determine if it is a palindrome.
"""

from leetCodeUtil import ListNode

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None:
            return True

        fast = slow = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        slow = self.reverseList(slow)

        while head is not None:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next

        return True


    def reverseList(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head

