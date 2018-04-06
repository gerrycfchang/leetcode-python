# 179. Largest Number
# 
# Given a list of non negative integers, arrange them such that they form the largest number.
# 
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.


class Solution(object):
    def largestNumber2(self, nums):
        for i in range(len(nums)):
            minIdx = i
            for j in range(i+1, len(nums)):
                if not self.compare(nums[minIdx], nums[j]):
                    minIdx = j
            nums[i], nums[minIdx] = nums[minIdx], nums[i]
        return str(int(''.join(map(str, nums))))

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)

if __name__ == '__main__':
    sol = Solution()
    assert sol.largestNumber2([3, 30, 34, 5, 9]) == '9534330'
    assert sol.largestNumber2([0,0]) == '0'