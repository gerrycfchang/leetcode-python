# 382. Linked List Random Node
# 
# Given a singly linked list, return a random node's value from the linked list. 
# Each node must have the same probability of being chosen.
# 
# Follow up:
# What if the linked list is extremely large and its length is unknown to you? 
# Could you solve this efficiently without using extra space?
# 
# Example:
# 
# // Init a singly linked list [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
# 
# // getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
# solution.getRandom();


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.list = head
        self.length = 0
        curr = head
        while curr:
            self.length += 1
            curr = curr.next
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import random
        rand = random.uniform(0, self.length)
        i = 0
        curr = self.list
        while i < rand:
            i += 1
            curr = curr.next
            if curr is None:
                curr = self.list
        return curr.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

if __name__ == '__main__':
    head = ListNode(1)
    node1= ListNode(2)
    node2= ListNode(3)
    head.next = node1
    node1.next= node2

    obj = Solution(head)
    param_1 = obj.getRandom()