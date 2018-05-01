# 147. Insertion Sort List
#
# Sort a linked list using insertion sort.

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
        if not head: return None
        curr = head
        dummy = ListNode(0)
        dummy.next = head
        while curr.next:
            if curr.next.val < curr.val:
                pre = dummy
                while pre.next.val < curr.next.val:
                    pre = pre.next
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next
        return dummy.next
        

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
