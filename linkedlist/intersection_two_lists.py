"""
For example, the following two linked lists:

A:          a1 > a2

                     c1 > c2 > c3

B:     b1 > b2 > b3
begin to intersect at node c1.


"""
import sys
sys.path.append('../')
from leetCodeUtil import ListNode


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        pA = headA
        pB = headB

        pCross = None

        while pCross is None:
            if pA and pB:
                if pA == pB:
                    pCross = pA
                else:
                    if pA.next is None and pB.next is None:
                        break
                    else:
                        if pA.next:
                            pA = pA.next
                        else:
                            pA = headB
                        if pB.next:
                            pB = pB.next
                        else:
                            pB = headA
        return pCross

