"""

"""

from leetCodeUtil import TreeNode

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.constructTree(nums, 0, len(nums))
        return root

    def constructTree(self, nums, start, end):

        if start >= end:
            return
        mid = start + int((end-start)/2)
        node = TreeNode(nums[mid])
        node.left = self.constructTree(nums, start, mid)
        node.right = self.constructTree(nums, mid+1, end)

        return node
