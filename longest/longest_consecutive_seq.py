"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlength = 0
        numset = set(nums)
        for n in nums:
            count = 0
            if len(numset) == 0:
                break

            val = n
            while val in numset:
                numset.remove(val)
                val += 1
                count += 1

            val = n - 1
            while val in numset:
                numset.remove(val)
                count += 1
                val -= 1

            maxlength = max(maxlength, count)
        return maxlength

if __name__ == '__main__':
    sol = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    assert (sol.longestConsecutive(nums) == 4)