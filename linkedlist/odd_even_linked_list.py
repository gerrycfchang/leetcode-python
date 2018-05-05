# 328. Odd Even Linked List
# 
# Given a singly linked list, group all odd nodes together followed by the even nodes. 
# Please note here we are talking about the node number and not the value in the nodes.
# 
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
# 
# Example:
# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.


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
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        odd, even = ListNode(-1), ListNode(-1)
        pointer, i = head, 1
        evenIndex = even
        while pointer:
            if i % 2 == 1:
                odd.next = pointer
                pointer = pointer.next
                odd = odd.next
                odd.next = None
            else:
                evenIndex.next = pointer
                pointer = pointer.next
                evenIndex = evenIndex.next
                evenIndex.next = None
            i += 1
            #pointer = pointer.next
        odd.next = even.next
        return head


if __name__ == '__main__':
    obj = Solution()
    tc1 = ListNode(1)
    head = obj.oddEvenList(tc1)
    assert list(head) == [1]


    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    head = obj.oddEvenList(head)
    assert list(head) == [1, 3, 5, 2, 4]