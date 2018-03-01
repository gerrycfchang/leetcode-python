"""
Given a string S, we can transform every letter individually to be lowercase or uppercase 
to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
"""

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        self.permute(S, 0, res)            
        return list(res)
    
    def permute(self, S, idx, res):
        #if S == '': return
        if S not in res:
            res.append(S)
        if idx >= len(S) or len(S) == 0: return
        #for i in range(idx+1, len(S)):
        self.permute(S, idx+1, res)
        if S[idx].islower():
            t = S[:idx] + S[idx].upper() + S[idx+1:]
        else:
            t = S[:idx] + S[idx].lower() + S[idx+1:]
        self.permute(t, idx+1, res)
        
        
if __name__ == '__main__':
    sol = Solution()
    exp = ["a1b2", "a1B2", "A1b2", "A1B2"]
    assert sol.letterCasePermutation('a1b2') == exp

    assert sol.letterCasePermutation('') == ['']

    assert sol.letterCasePermutation('C') == ['C', 'c']

    assert sol.letterCasePermutation('12345') == ['12345']