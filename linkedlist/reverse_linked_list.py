# 206. Reverse Linked List

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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        
        while head is not None:                       
            p = head
            head = head.next
            p.next = new_head
            new_head = p            
        return new_head


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

    head = obj.reverseList(head)
    assert list(head) == [5,4,3,2,1]

        