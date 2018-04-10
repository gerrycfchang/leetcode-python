"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

"""


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False

        slow = fast = head
        isCycle = False

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                isCycle = True
                break
        return isCycle