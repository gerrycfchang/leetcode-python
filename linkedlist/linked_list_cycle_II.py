"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

"""


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return None

        slow = fast = head
        isCycle = False

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                isCycle = True
                break

        if not isCycle: return None

        p = head
        while p != slow:
            p = p.next
            slow = slow.next
        return p