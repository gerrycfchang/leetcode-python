# 645. Set Mismatch
# 
# The set S originally contains numbers from 1 to n. 
# But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, 
# which results in repetition of one number and loss of another number.
# 
# Given an array nums representing the data status of this set after the error. 
# Your task is to firstly find the number occurs twice and then find the number that is missing. 
# Return them in the form of an array.
# 
# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]

import collections
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n, res, c = len(nums), [], collections.Counter(nums)
        total = ((1 + n) * n)/2
        for key, value in c.items():
            if value == 2:
                res.append(key)
                break
        res.append(total-(sum(nums)-res[0]))
        return res
        
if __name__ == "__main__":
    sol = Solution()
    assert sol.findErrorNums([1, 2, 2, 4]) == [2, 3]