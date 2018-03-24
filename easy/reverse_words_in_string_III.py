# 557. Reverse Words in a String III
# 
# Given a string, you need to reverse the order of characters in each word 
# within a sentence while still preserving whitespace and initial word order.
# 
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = s.split()
        res = [s[::-1] for s in slist]
        return ' '.join(res)
        

if __name__ == '__main__':
    sol = Solution()
    assert sol.reverseWords("Let's take LeetCode contest") == 's\'teL ekat edoCteeL tsetnoc'