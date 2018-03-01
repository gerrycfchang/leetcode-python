"""
Given a list of sorted characters letters containing only lowercase letters,
and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and 
letters = ['a', 'b'], the answer is 'a'.
"""

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        idx = 0
        res = float('inf')
        for i in range(len(letters)):
            diff = (ord(letters[i]) - ord(target))
            if diff > 0:
                if diff < res:
                    res, idx = diff, i                
        if diff < 0:
            return letters[0]
        else:
            return letters[idx]

if __name__ == '__main__':
    sol = Solution()
    nums = ["c", "f", "j"]
    assert sol.nextGreatestLetter(nums, 'a') == 'c'

    nums = ["a", "b"]
    assert sol.nextGreatestLetter(nums, 'z') == 'a'

    nums = ["c", "f", "j"]
    assert sol.nextGreatestLetter(nums, 'c') == 'f'