class Solution(object):
    def findMinSol(self, num):
        import math
        dp = [float('inf') for x in range (num+1)]
        dp [1] = 1
        dp [2] = 2
        for i in range (3, num+1):
            sq = int(math.sqrt(i))
            if sq * sq == i:
                dp[i] = 1
            else:
                for j in range (1, i/2+1):
                    dp[i] = min(dp[i], dp[j]+dp[i-j])
        return dp[num]

if __name__ == '__main__':
    sol = Solution()
    assert sol.findMinSol(4) == 1
    assert sol.findMinSol(5) == 2
    assert sol.findMinSol(11) == 3
    assert sol.findMinSol(12) == 3
