# 2. Add Two Numbers
# 
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# Example
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807


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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        elif l1 and l2 is None:
            return l1
        elif l1 is None and l2:
            return l2

        result = ListNode(-1)
        self.caculateValue(result, l1, l2, 0)
        return result.next

    def caculateValue(self, result, l1, l2, add):
        node = ListNode(0)
        isAdded = 0
        value = 0

        if l1 and l2:
            if l1.val + l2.val + add >= 10:
                value = l1.val + l2.val + add - 10
                isAdded = 1
            else:
                value = l1.val + l2.val + add
        elif l1:
            if l1.val + add >= 10:
                value = l1.val + add - 10
                isAdded = 1
            else:
                value = l1.val + add
        elif l2:
            if l2.val + add >= 10:
                value = l2.val + add - 10
                isAdded = 1
            else:
                value = l2.val + add
        elif l1 is None and l2 is None and add == 1:
            value = 1
        else:
            return

        node.val = value
        result.next = node

        if l1 and l2:
            self.caculateValue(node, l1.next, l2.next, isAdded)
        elif l1:
            self.caculateValue(node, l1.next, None, isAdded)
        elif l2:
            self.caculateValue(node, None, l2.next, isAdded)
        elif l1 is None and l2 is None and add == 1:
            self.caculateValue(node, None, None, isAdded)


if __name__ == '__main__':
    obj = Solution()
    head1 = ListNode(2)
    node1 = ListNode(4)
    node2 = ListNode(3)
    head1.next = node1
    node1.next = node2

    head2 = ListNode(5)
    node4 = ListNode(6)
    node5 = ListNode(4)    
    head2.next = node4
    node4.next = node5

    head = obj.addTwoNumbers(head1, head2)
    assert list(head) == [7, 0, 8]