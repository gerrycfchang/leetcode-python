# 143. Reorder List
# 
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# You may not modify the values in the list's nodes, only nodes itself may be changed.
# 
# Example 1:
# 
# Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:
# 
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head: return
        fast = slow = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        second = self.reverseList(second)
        self.mergeList(head, second)

    def reverseList(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head

    def mergeList(self, first, second):
        while second:
            next1, next2=first.next, second.next
            first.next=second
            second.next=next1
            first, second=next1, next2
        

if __name__ == "__main__":
    sol = Solution()
    # Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    sol.reorderList(node1)
    assert list(node1) == [1, 5, 2, 4, 3]
