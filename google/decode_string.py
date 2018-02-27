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

    def decodeString(self, str):
        index = [0]
        res = self.decode(str, index)
        return res

    def decode(self, str, index):
        res = ''
        while index[0] < len(str) and str[index[0]] != ']':
            if str[index[0]] < '0' or str[index[0]] > '9':
                res += str[index[0]]
                index[0] += 1
            else:
                cnt = 0
                while index[0] < len(str) and str[index[0]] >= '0' and str[index[0]] <= '9':
                    cnt = cnt * 10 + int(str[index[0]])
                    index[0] += 1
                index[0] += 1
                t = self.decode(str, index)
                res += t * cnt
                index[0] += 1
        return res


if __name__ == '__main__':
    sol = Solution()

    assert(sol.decompress('a3[b2[c1[d]]]e') == 'abcdcdbcdcdbcdcde')
    assert(sol.decompress('3[a]2[bc]') == 'aaabcbc')
    assert(sol.decompress('3[a2[c]]') == 'accaccacc')
    assert(sol.decompress('2[abc]3[cd]ef') == 'abcabccdcdcdef')
    assert(sol.decompress('abcdef') == 'abcdef')
    assert(sol.decompress('10[ab]') == 'abababababababababab')
    assert(sol.decodeString('10[ab]') == 'abababababababababab')
    assert(sol.decodeString('2[abc]3[cd]ef') == 'abcabccdcdcdef')



