# 19. Remove Nth Node From End of List
# 
# Given a linked list, remove the nth node from the end of list and return its head.
# 
# For example,
# 
#    Given linked list: 1->2->3->4->5, and n = 2.
# 
#    After removing the second node from the end, the linked list becomes 1->2->3->5.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __iter__(self):
        item = self
        while item is not None:
            yield item.val
            item = item.next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = prehead = ListNode(0)
        prehead.next = head
        while fast.next:
            if n:
                n -= 1
            else:
                slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return prehead.next


if __name__ == "__main__":
    sol = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    res = sol.removeNthFromEnd(node1, 2)
    assert list(res) == [1,2,3,5]
        
                
            