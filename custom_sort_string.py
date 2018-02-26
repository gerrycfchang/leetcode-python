"""
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid output
"""

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        from collections import Counter
        c = Counter(T)
        res1, res2 = [], []
        for i in range(len(S)):
            tmp = c[S[i]] * S[i]
            res1.append(tmp)
            
        for i in range (len(T)):
            if T[i] not in S:
                res2.append(T[i])
            
        return ''.join(res1) + ''.join(res2)
if __name__ == '__main__':
    sol = Solution()
    S = "cba"
    T = "abcd"
    assert sol.customSortString (S, T) == 'cbad'

    S = "kqep"
    T = "pekeq"
    res = sol.customSortString (S, T)
    assert  res == 'kqeep'