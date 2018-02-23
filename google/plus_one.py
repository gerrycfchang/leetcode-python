"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.


"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        self.calculateNum(digits, len(digits) - 1)
        return digits

    def calculateNum(self, digits, index):
        if index == -1:
            digits.insert(0, 0)
            index = 0

        if digits[index] <= 8:
            digits[index] = digits[index] + 1
        else:
            digits[index] = 0
            self.calculateNum(digits, index - 1)

        return

if __name__ == '__main__':
    sol = Solution()

    exp = [1]
    assert (sol.plusOne([0]) == exp)

    exp = [1,0]
    assert(sol.plusOne([9]) == exp)

    exp = [1,0,0]
    assert (sol.plusOne([9,9]) == exp)