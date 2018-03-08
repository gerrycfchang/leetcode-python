# 795. Number of Subarrays with Bounded Maximum
#
# We are given an array A of positive integers, and two positive integers L and R (L <= R).
# 
# Return the number of (contiguous, non-empty) subarrays 
# 
# such that the value of the maximum array element in that subarray is at least L and at most R.
# 
# Example :
# Input: 
# A = [2, 1, 4, 3]
# L = 2
# R = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        dp = [0 for _ in range(len(A) + 1)]
        prev = -1
        for i in range(1,len(A) + 1):
            if A[i-1] < L:
                dp[i] = dp[i-1]
            # No valid sub-array ending with this char
            # Use prev record the position
            elif A[i-1] > R:
                dp[i] = 0
                prev = i-1
            # Any sub-array starts after the previous invalid number end with this char is valid
            # A[prev + 1 ~ i], A[prev + 2 ~ i]... are all valid
            elif L <= A[i-1] <= R:
                dp[i] = (i-1) - prev
        return sum(dp)

if __name__ == '__main__':
    sol = Solution()
    A = [2, 1, 4, 3]
    assert sol.numSubarrayBoundedMax(A, 2, 3) == 3

    A = [2,9,2,5,6]
    assert sol.numSubarrayBoundedMax(A, 2, 8) == 7