# 148. Sort List
# Sort a linked list in O(n log n) time using constant space complexity.
#
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
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head   
        slow = fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)
    
    def merge(self, l, r):
        if not l or not r:
            return l or r
        if l.val > r.val:
            l, r = r, l
        pre = head = l
        l = l.next
        while l and r:
            if l.val < r.val:
                pre.next = l
                l = l.next
            else:
                pre.next = r
                r = r.next
            pre = pre.next
        pre.next = l or r
        return head

if __name__ == "__main__":
    sol = Solution()
    node1 = ListNode(6)
    node2 = ListNode(5)
    node3 = ListNode(4)
    node4 = ListNode(3)
    node5 = ListNode(2)
    node6 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    res = sol.sortList(node1)
    assert list(res) == [1,2,3,4,5,6]
