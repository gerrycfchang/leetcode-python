# 8. String to Integer (atoi)

import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        try:
            str = str.strip()
            str = re.findall('^[+\-]?\d+', str)
            inp = int(''.join(str))
            if inp > 2147483647:
                return 2147483647
            elif inp < -2147483648:
                return -2147483648
            else:
                return inp
        except:
            return 0
        
        
if __name__ == '__main__':
    sol  = Solution()
    assert sol.myAtoi('') == 0