from leetCodeUtil import ListNode

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
