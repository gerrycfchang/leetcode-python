class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ## Time exceed limit
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        
        for i in range (1, amount+1):
            if i in coins:
                dp[i] = 1
            else:
                for j in range(1, i/2+1):
                    dp[i] = min(dp[i], dp[j]+dp[i-j])
        
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
        
    
    def coinChangeSol(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        
        for i in range (1, amount+1):
            for j in range (len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        print dp[amount]
        if dp[amount] > amount:
            return -1
        else:
            return dp[amount]



if __name__ == '__main__':
    sol = Solution()
    coins = [1]
    assert sol.coinChange(coins, 2) == 2
    assert sol.coinChange([1], 0) == 0
    assert sol.coinChange([2], 1) == -1
    assert sol.coinChangeSol([3,7,405,436], 8839) == 25