"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.

"""

class Solution(object):
    def isStrobogrammatic(self, x):
        stroNum = 0
        validNumber = [0, 1, 6, 8, 9]
        while x > stroNum:
            val = x % 10
            if not (val in validNumber):
                return False
            elif val == 6:
                val = 9
            elif val == 9:
                val = 6
            stroNum = stroNum * 10 + val
            x /= 10


        if stroNum > x:
            lastNumber = stroNum % 10
            if lastNumber not in [0, 1, 8]:
                return False
            stroNum /= 10

        if x == stroNum:
            return True

if __name__ == '__main__':
    sol = Solution()
    assert (sol.isStrobogrammatic(13) == False)
    assert (sol.isStrobogrammatic(16791) == False)
    assert (sol.isStrobogrammatic(69) == True)
    assert (sol.isStrobogrammatic(88) == True)
    assert (sol.isStrobogrammatic(8008) == True)
    assert (sol.isStrobogrammatic(8698) == True)
    assert (sol.isStrobogrammatic(1691) == True)
    assert (sol.isStrobogrammatic(818) == True)
    assert (sol.isStrobogrammatic(916) == True)
    assert (sol.isStrobogrammatic(986) == True)
    assert (sol.isStrobogrammatic(101) == True)
    assert (sol.isStrobogrammatic(609) == True)
    assert(sol.isStrobogrammatic(8) == True)
    assert(sol.isStrobogrammatic(669) == False)