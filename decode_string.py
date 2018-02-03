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
        index = [0]
        i = 0

        while i < len(str):
            c = str[i]
            if c.isdigit():
                index[0] = i
                stack_nums.append(self.getNumber(str, index))
                i = index[0]
            elif c == '[':
                string.append(stack_curr)
                stack_curr = []
            elif c == ']':
                string[-1].extend(stack_curr * stack_nums.pop())
                stack_curr = string.pop()
            else:
                stack_curr.append(c)
            i += 1
        return "".join(string[-1]) if string else "".join(stack_curr)

    def getNumber(self, str, index):
        numStr = ''
        i = index[0]
        while i < len(str):
            if str[i].isdigit():
                numStr += str[i]
                i += 1
            else:
                break
        index[0] = i - 1
        return int(numStr)



