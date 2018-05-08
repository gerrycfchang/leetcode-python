# 83. Remove Duplicates from Sorted List
# 
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# 
# Example 1:
# 
# Input: 1->1->2
# Output: 1->2
# Example 2:
# 
# Input: 1->1->2->3->3
# Output: 1->2->3

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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        phead = dummy
        duplicate = phead.next
        while phead.next:
            while duplicate.next and duplicate.val == duplicate.next.val:
                duplicate = duplicate.next
            phead.next = duplicate
            phead = phead.next
            duplicate = phead.next
        return dummy.next


if __name__ == '__main__':
    obj = Solution()
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(4)
    node6 = ListNode(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    head = obj.deleteDuplicates(head)
    assert list(head) == [1, 2, 3, 4, 5]

    head = ListNode(1)
    node1 = ListNode(1)
    node2 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(5)
    head.next = node1
    node1.next = node2
    node2.next = node5
    node5.next = node6
    head = obj.deleteDuplicates(head)
    assert list(head) == [1, 3, 4, 5]