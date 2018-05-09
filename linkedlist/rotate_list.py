# 61. Rotate List
# 
# Given a linked list, rotate the list to the right by k places, where k is non-negative.
# 
# Example 1:
# 
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# Example 2:
# 
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL


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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or not head: return head
        dummy = ListNode(-1)
        dummy.next = head
        length = 0
        while dummy.next:
            length += 1
            dummy = dummy.next
        dummy.next = head      
        
        steps = length - k % length - 1
        p = head
        for i in range(steps):
            p = p.next          
        head = p.next
        p.next = None
        return head


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

    head = obj.rotateRight(head, 2)
    assert list(head) == [4, 5, 1, 2, 3]

    head = obj.rotateRight(ListNode(1), 1)
    assert list(head) == [1]

    head = ListNode(1)
    node = ListNode(2)
    head.next = node
    head = obj.rotateRight(head, 1)
    assert list(head) == [2, 1]
