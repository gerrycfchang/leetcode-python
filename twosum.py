class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for x in range(0, len(nums)):
            for y in range(x+1, len(nums)):
                sum = nums[x] + nums[y]
                if sum == target:
                    print "x,y", x, y
                    result.append(x)
                    result.append(y)
                    break
                else:
                    continue
                break
            else:
                continue
            break
        return result


if __name__ == '__main__':
    nums = [0, 7, 11, 15]
    target = 15
    test = Solution()
    rlist = test.twoSum(nums, target)
    print rlist
