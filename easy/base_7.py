class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        res = []
        if num < 0:
            inp = num * -1
        else:
            inp = num
        while inp > 0:
            val = inp % 7
            res.append(str(val))
            inp //= 7
        return ''.join(res[::-1]) if num >=0 else '-'+''.join(res[::-1])

if __name__ == '__main__':
    sol = Solution()
    assert sol.convertToBase7(100) == '202'
    assert sol.convertToBase7(0) == '0'
    assert sol.convertToBase7(-7) == '-10'