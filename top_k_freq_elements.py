"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        import heapq
        c = Counter()
        for num in nums:
            c[num] += 1
        heap = []

        for key, value in c.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else:
                if heap[0][0] < value:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (value, key))

        return [x[1] for x in heap]

