class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) == 0: return None
        self.tree = [0 for _ in range(len(nums) + 1)]
        self.nums = nums
        for i in range (1, len(self.tree)):
            self.add(i, nums[i-1])
            
    def add(self, i, val):
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.add(i + 1, val - self.nums[i])
        self.nums[i] = val
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum(j+1) - self.sum(i)
    
    def sum(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

if __name__ == '__main__':
    
    nums = [-2, 0, 3, -5, 2, -1]
    na = NumArray(nums)
    assert na.sumRange(0, 2) == 1
    
    nums = [1, 3, 5]
    assert na.sumRange(0, 2) == 9
    na.update(1, 2)
    assert na.sumRange(0, 2) == 8