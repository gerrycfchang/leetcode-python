# 654. Maximum Binary Tree
#
# Given an integer array with no duplicates. 
# A maximum tree building on this array is defined as follow:
# 
# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.
# 
# Example 1:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
# 
#       6
#     /   \
#    3     5
#     \    / 
#      2  0   
#        \
#         1


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.right = None
        self.seqlist = []

    def __str__(self):
        self.inorder(self)
        return ' '.join(str(x) for x in self.seqlist)

    def inorder(self, curr):
        if not curr: return
        self.inorder(curr.left)
        self.seqlist.append(curr.val)
        self.inorder(curr.right)

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if len(nums) == 0: return None
        root = TreeNode(max(nums))
        root.left  = self.constructMaximumBinaryTree(nums[0:nums.index(max(nums))])
        root.right = self.constructMaximumBinaryTree(nums[nums.index(max(nums))+1:])
        return root


if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,1,6,0,5]
    root = sol.constructMaximumBinaryTree(nums)
    assert str(root) == ' '.join(str(x) for x in nums)
            
        