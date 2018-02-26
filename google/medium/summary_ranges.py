"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        rlist = []
        if len(nums) == 0: return []
        i = 0
        while i < len(nums):
            res = []
            res.append(nums[i])
            while i != len(nums) - 1 and nums[i + 1] - nums[i] == 1:
                res.append(nums[i + 1])
                i += 1
            if len(res) > 1:
                rlist.append(str(res[0]) + '->' + str(res[-1]))
            else:
                rlist.append(str(res[0]))
            i += 1
        return rlist


if __name__ == '__main__':
    sol = Solution()

    nums = [0,1,2,4,5,7]
    exp = ["0->2","4->5","7"]
    assert(sol.summaryRanges(nums) == exp)

    nums = [0,2,3,4,6,8,9]
    exp = ["0","2->4","6","8->9"]
    assert(sol.summaryRanges(nums) == exp)