# 686. Repeated String Match

# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. 
# If no such solution, return -1.
# 
# For example, with A = "abcd" and B = "cdabcdab".
# 
# Return 3, because by repeating A three times ("abcdabcdabcd"), 
# 
# B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(A) == 0: return -1
        t, cnt = A, 1
        while len(t) < len(B):
            t += A
            cnt += 1
        if t.find(B) >= 0: return cnt
        t += A
        cnt += 1
        return cnt if t.find(B) >= 0 else -1

if __name__ == '__main__':
    sol = Solution()
    assert sol.repeatedStringMatch('a', 'aa') == 2
    assert sol.repeatedStringMatch('abcd', 'cdabcdab') == 3
    assert sol.repeatedStringMatch('abababaaba', 'aabaaba') == 2
    assert sol.repeatedStringMatch('baa', 'abaab') == 3
        