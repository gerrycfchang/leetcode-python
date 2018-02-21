"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
sys.path.append('../')
from leetCodeUtil import ListNode
from leetCodeUtil import TreeNode

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return None
        if not head.next: return TreeNode(head.val)
        
        slow = fast = last = head
        while fast.next is not None and fast.next.next is not None:
            last = slow
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        last.next = None
        
        cur = TreeNode(slow.val)
        if head != slow:
            cur.left = self.sortedListToBST(head)
        cur.right = self.sortedListToBST(fast)
        return cur
        
if __name__ == '__main__':
    sol = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    result = sol.sortedListToBST(node1)
    exp1 = [1, 2, None, 3, None, 4, 5]
    assert result == exp1