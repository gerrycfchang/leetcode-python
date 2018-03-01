"""

"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        while n != 0:
            result = chr(65 + ((n-1) % 26)) + result
            n = (n-1) / 26

        return result

if __name__ == '__main__':
    sol = Solution()
    assert (sol.convertToTitle(1) == 'A')
    assert (sol.convertToTitle(27) == 'AA')
    assert (sol.convertToTitle(512) == 'SR')