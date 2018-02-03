"""

Given a compressed string in which a number followed by [] indicate how many times those characters occur, decompress the string
Eg. : a3[b2[c1[d]]]e will be decompressed as abcdcdbcdcdbcdcde.

"""
import collections

class Solution(object):
    def decompress(self, str):

        stack_nums = []
        stack_curr = []
        string = []

        for c in str:
            if c.isdigit():
                stack_nums.append(int(c))
            elif c == '[':
                string.append(stack_curr)
                stack_curr = []
            elif c == ']':
                string[-1].extend(stack_curr * stack_nums.pop())
                stack_curr = string.pop()
            else:
                stack_curr.append(c)
        return "".join(string[-1]) if string else "".join(stack_curr)



