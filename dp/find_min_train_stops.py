"""
There are an infinite number of train stops starting from station number 0.

There are an infinite number of trains. The nth train stops at all of the k * 2^(n - 1) stops where k is between 0 and infinity.

When n = 1, the first train stops at stops 0, 1, 2, 3, 4, 5, 6, etc.

When n = 2, the second train stops at stops 0, 2, 4, 6, 8, etc.

When n = 3, the third train stops at stops 0, 4, 8, 12, etc.

Given a start station number and end station number, return the minimum number of stops between them. You can use any of the trains to get from one stop to another stop.

For example, the minimum number of stops between start = 1 and end = 4 is 3 because we can get from 1 to 2 to 4.
"""

class Solution(object):
    def findMinTrainStops(self,start, end):
        dp = [0 for _ in range(end+1)]
        dp[0], dp[1] = 0, 1
        for i in range (2, end+1):
            j = 2
            m = dp[i-1]
            while i - j >= start:
                if i%j == 0:
                    m = min(m, dp[i-j])
                j <<= 1
            dp[i] = m + 1
        return dp[end]

if __name__ == '__main__':
    test = Solution()
    assert test.findMinTrainStops(1, 4) == 3
    assert test.findMinTrainStops(1, 8) == 4
