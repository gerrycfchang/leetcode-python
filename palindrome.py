"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        Number = 0
        if x < 0 or (x % 10 ==0 and x != 0):
            return False
        else:
            while (x > Number):
                Number = Number * 10 + x % 10
                x = x / 10

            if x == Number or (Number / 10) == x:
                return True
            else:
                return False


if __name__ == "__main__":
    sol = Solution()
    print sol.isPalindrome(0)
    print sol.isPalindrome(30)
    print sol.isPalindrome(121)
    print sol.isPalindrome(12321)
    print sol.isPalindrome(1221)
