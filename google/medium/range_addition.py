"""

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