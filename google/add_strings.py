"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        index1, index2, digit, carry = len(num1), len(num2), 0, 0
        result = []

        while index1 or index2 or carry:
            digit = 0
            if index1:
                digit += int(num1[index1 - 1])
                index1 -= 1
            if index2:
                digit += int(num2[index2 - 1])
                index2 -= 1

            digit += carry
            carry = 0
            if digit > 9:
                carry = 1
            result.append(str(digit % 10))

        return "".join(result[::-1])
