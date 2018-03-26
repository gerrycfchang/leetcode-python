# 485. Max Consecutive Ones
# 
# Given a binary array, find the maximum number of consecutive 1s in this array.
# 
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp, maxNum = 0, 0
        for num in nums:
            if num == 1:
                dp += 1
            else:
                maxNum = max(dp, maxNum)
                dp = 0
        return max(maxNum, dp)
        
    def antoherSol(self, nums):
        return max(map(lambda x: len(x), ''.join(str(i) for i in nums).split('0')))
if __name__ == '__main__':
    sol = Solution()
    assert sol.findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3
    assert sol.antoherSol([1,1,0,1,1,1]) == 3
    assert sol.antoherSol([1,1,0,1,1,1,1,0]) == 4
    assert sol.antoherSol([0]) == 0