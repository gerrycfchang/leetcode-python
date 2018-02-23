"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]
"""

class Solution(object):
    def combinationSumIII(self, k, n):
        Solution.ret = []
        self.dfs(k, n, 1, [])
        return Solution.ret


    def dfs(self, k, taget, start, valuelist):
        if k == 0 and taget == 0 and valuelist not in Solution.ret:
            Solution.ret.append(valuelist)
        for i in range (start, 10):
            if taget < i:
                return
            self.dfs(k - 1, taget - i, i + 1, valuelist + [i])

if __name__ == '__main__':
    sol = Solution()

    exp = [[1,2,4]]
    assert(sol.combinationSumIII(3, 7) == exp)

    exp = [[1,2,6], [1,3,5], [2,3,4]]
    assert(sol.combinationSumIII(3, 9) == exp)

    exp = []
    assert(sol.combinationSumIII(2, 18) == exp)

    exp = [[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]]
    assert(sol.combinationSumIII(3, 15) == exp)