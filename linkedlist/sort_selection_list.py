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
        curr = dummy = ListNode(0)
        dummy.next = head
        
        while curr.next:
            premin = pre = curr
            while pre.next:
                if pre.next.val < premin.next.val:
                    premin = pre
                pre = pre.next
            # swap curr.next & premin.next
            self.swap(curr, premin)
            curr = curr.next
        return dummy.next

    def swap(self, curr, premin):
            #premin.next.val, curr.next.val = curr.next.val, premin.next.val
            next1, next2, t2 = curr.next.next, premin.next.next, premin.next
            if next1 != t2:
                curr.next.next = next2
                premin.next = curr.next
                t2.next = next1            
                curr.next = t2
            else:
                curr.next = t2
                premin.next = next2
                t2.next = premin       


if __name__ == "__main__":
    sol = Solution()
    # Test case 1: 6 > 5 > 4 > 3 > 2 > 1
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

    # Test case 2: 1 > 2 > 4 > 3
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)
    node4 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    res = sol.sortList(node1)
    assert list(res) == [1,2,3,4]

    # Test case 3: 1
    res = sol.sortList(ListNode(1))
    assert list(res) == [1]


            