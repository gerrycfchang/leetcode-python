"""
Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:

Given:

    length = 5,
    updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]
    ]

Output:

    [-2, 0, 3, 5, 3]
Explanation:

Initial state:
[ 0, 0, 0, 0, 0 ]

After applying operation [1, 3, 2]:
[ 0, 2, 2, 2, 0 ]

After applying operation [2, 4, 3]:
[ 0, 2, 5, 5, 3 ]

After applying operation [0, 2, -2]:
[-2, 0, 3, 5, 3 ]
Hint:

Thinking of using advanced data structures? You are thinking it too complicated.
For each update operation, do you really need to update all elements between i and j?
Update only the first and end element is sufficient.
The optimal time complexity is O(k + n) and uses O(1) extra space.

"""

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """

        result = [0 for x in range(length)]
        if length == 0: return result
        for i in range(len(updates)):
            start = updates[i][0]
            end = updates[i][1]
            opt = updates[i][2]
            result[start] += opt
            if end < length - 1:
                result[end+1] -= opt
        sum = 0
        for i in range (len(result)):
            sum += result[i]
            result[i] = sum
        return result

        """
        for i in range (len(updates)):
            start = updates[i][0]
            end   = updates[i][1]
            opt   = updates[i][2]
            for j in range (start, end+1):
                result[j] += opt

        return result
        """

if __name__ == '__main__':
    sol = Solution()

    updates = [
            [1, 3, 2],
            [2, 4, 3],
            [0, 2, -2]
        ]
    result = sol.getModifiedArray(5, updates)
    assert (result == [-2, 0, 3, 5, 3])

    updates = [
                [1, 3, 2],
                [2, 4, 3],
                [0, 2, -2]
            ]
    result = sol.getModifiedArray(0, updates)
    assert (result == [])

    updates = [
                [0, 0, 1]
            ]

    result = sol.getModifiedArray(1, updates)
    assert (result == [1])