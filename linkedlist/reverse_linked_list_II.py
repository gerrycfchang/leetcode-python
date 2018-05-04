# 92. Reverse Linked List II
# 
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL


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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head: return None
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        for i in range(m-1):
            prev = prev.next

        curr = prev.next
        newHead = curr
        for i in range(n-m):
            nextNode = curr.next
            nextLink = nextNode.next
            nextNode.next = newHead
            newHead = nextNode
            curr.next = nextLink
        prev.next = newHead
        return dummy.next
        

if __name__ == '__main__':
    obj = Solution()
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    head = obj.reverseBetween(head, 2, 4)
    assert list(head) == [1, 4, 3, 2, 5]