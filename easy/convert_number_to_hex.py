class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {10: 'a', 11: 'b', 12:'c', 13:'d', 14: 'e', 15: 'f'}
        if num == 0: return '0'
        if num <  0: num += 2**32
        res = []
        while num > 0:
            val = num % 16
            num //= 16
            if val in dic:
                res.append(dic[val])
            else:
                res.append(str(val))
        return ''.join(res[::-1])

if __name__ == '__main__':
    sol = Solution()
    assert sol.toHex(26) == '1a'
    assert sol.toHex(0) == '0'  
    assert sol.toHex(-1) == 'ffffffff'