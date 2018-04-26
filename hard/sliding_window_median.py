# 480. Sliding Window Median
# 
# Median is the middle value in an ordered integer list. 
# If the size of the list is even, there is no middle value. 
# So the median is the mean of the two middle value.
# 
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
# 
# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7       3
#  1  3  -1  -3 [5  3  6] 7       5
#  1  3  -1  -3  5 [3  6  7]      6
# Therefore, return the median sliding window as [1,-1,-1,3,5,6].


import bisect
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        res = []
        win = sorted(nums[:k])
        res.append((win[k//2] + win[k//2-1])/2. if k%2 == 0 else win[k//2] * 1.)
        for i in range(len(nums) - k):
            win.remove(nums[i])
            bisect.insort(win, nums[k+i])
            res.append((win[k//2] + win[k//2-1])/2. if k%2 == 0 else win[k//2] * 1.)
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.medianSlidingWindow([2147483647,2147483647], 2) == [2147483647.0]
    assert sol.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [1.0,-1.0,-1.0,3.0,5.0,6.0]