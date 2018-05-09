# 445. Add Two Numbers II
# 
# You are given two non-empty linked lists representing two non-negative integers. 
# The most significant digit comes first and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
# 
# Example:
# 
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __iter__(self):
        item = self
        while item is not None:
            yield item.val
            item = item.next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = self.convert(l1) + self.convert(l2)
        return self.intToLinkedList(result)

    def convert(self, l1):
        num = []
        p = l1
        while p:
            num.append(str(p.val))
            p = p.next
        return int(''.join(num))

    def intToLinkedList(self, num):
        s_num = str(num)
        head = ListNode(-1)
        p = head
        
        for c in s_num:
            p.next = ListNode(int(c))
            p = p.next       
        return head.next


if __name__ == '__main__':
    obj = Solution()
    head1 = ListNode(7)
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    head1.next = node1
    node1.next = node2
    node2.next = node3

    head2 = ListNode(5)
    node4 = ListNode(6)
    node5 = ListNode(4)    
    head2.next = node4
    node4.next = node5

    head = obj.addTwoNumbers(head1, head2)
    assert list(head) == [7, 8, 0, 7]
