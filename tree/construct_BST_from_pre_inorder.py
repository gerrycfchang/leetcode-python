# 105. Construct Binary Tree from Preorder and Inorder Traversal
# 
# Given preorder and inorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """        
        res =  self.construct(preorder, inorder)
        return res
        
    def construct(self, preorder, inorder):
        if not preorder: return
        root = TreeNode(preorder[0])
        rootIdx = inorder.index(preorder[0])
        if rootIdx  > 0:
            root.left = self.construct(preorder[1:rootIdx+1], inorder[0:rootIdx])
        rightLastIdx = len(inorder) - 1
        if rightLastIdx > inorder.index(preorder[0]):            
            root.right = self.construct(preorder[rootIdx + 1:], inorder[rootIdx+1:])
        return root
        

if __name__ == '__main__':
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    sol = Solution()
    assert str(sol.buildTree(preorder, inorder)) == ' '.join(str(x) for x in inorder)

    preorder = [1,2]
    inorder = [1,2]
    sol = Solution()
    assert str(sol.buildTree(preorder, inorder)) == ' '.join(str(x) for x in inorder)

    preorder = [1,2]
    inorder = [2,1]
    sol = Solution()
    assert str(sol.buildTree(preorder, inorder)) == ' '.join(str(x) for x in inorder)

    preorder = [1,2,3]
    inorder = [3,2,1]
    sol = Solution()
    assert str(sol.buildTree(preorder, inorder)) == ' '.join(str(x) for x in inorder)

