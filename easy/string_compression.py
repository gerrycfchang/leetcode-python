# 443. String Compression
# 
# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.
# After you are done modifying the input array in-place, return the new length of the array.
# 
# Example 1:
# Input:
# ["a","a","b","b","c","c","c"]
# 
# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# 
# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
# Example 2:
# Input:
# ["a"]
# 
# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]
# 
# Explanation:
# Nothing is replaced.
# Example 3:
# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# 
# Output:
# Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# 
# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
# Notice each digit has it's own entry in the array.# 


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 1
        while i < len(chars):           
            count = 1
            while i < len(chars) and chars[i] == chars[i-1]:
                count += 1
                del chars[i]
            if count > 1: 
                for n in str(count):
                    chars.insert(i, n)
                    i += 1
                if i < len(chars) and chars[i] == chars[i-1]: i += 1
            else: i += 1
        return (chars)
                
                    
if __name__ == '__main__':
    sol = Solution()
    assert sol.compress(["a","a","b","b","c","c","c"]) == ['a', '2', 'b', '2', 'c', '3']
    assert sol.compress(["a"]) == ['a']
    assert sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]) == ['a', 'b', '1', '2']
    assert sol.compress(["a","a","a","b","b","a","a"]) == ['a', '3', 'b', '2', 'a', '2']
    assert sol.compress(["a","a","2","2","2"]) == ['a', '2', '2', '3']