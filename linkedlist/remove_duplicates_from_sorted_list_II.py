# 82. Remove Duplicates from Sorted List II
# 
# Given a sorted linked list, delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list.
# 
# Example 1:
# 
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# Example 2:
# 
# Input: 1->1->1->2->3
# Output: 2->3


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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        phead = dummy
        duplicate = phead.next
        isDup = False
        while phead.next:
            while duplicate.next and duplicate.val == duplicate.next.val:
                isDup = True
                duplicate = duplicate.next
            if isDup:
                phead.next = duplicate.next
            else:
                phead = phead.next                        
            isDup = False
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
    assert list(head) == [1, 2, 5]

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
    assert list(head) == [3, 4, 5]