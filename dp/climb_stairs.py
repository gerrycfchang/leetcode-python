"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = []
        table.append(1)
        table.append(1)
        table.append(2)

        for i in range(3, n + 1):
            value = table[i - 1] + table[i - 2]
            table.append(value)

        return table[n]