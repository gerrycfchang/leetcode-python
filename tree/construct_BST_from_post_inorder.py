# 106. Construct Binary Tree from Inorder and Postorder Traversal
# 
# Given inorder and postorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        res =  self.construct(inorder, postorder)
        return res

    def construct(self, inorder, postorder):
        if not postorder: return
        root = TreeNode(postorder[-1])
        rootIdx = inorder.index(postorder[-1]) # this means how many elements in left side
        if rootIdx  > 0:
            root.left = self.construct(inorder[0:rootIdx], postorder[0:rootIdx])        
        root.right = self.construct(inorder[rootIdx+1:], postorder[rootIdx:-1])
        return root

if __name__ == '__main__':

    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    postorder = [9,15,7,20,3]
    inorder = [9,3,15,20,7]
    sol = Solution()

    assert str(sol.buildTree(inorder, postorder)) == ' '.join(str(x) for x in inorder)
    
    #   1
    #    \
    #     2
    postorder = [2,1]
    inorder = [1,2]
    sol = Solution()
    assert str(sol.buildTree(inorder, postorder)) == ' '.join(str(x) for x in inorder)

    #   1
    #  /
    # 2
    postorder = [2,1]
    inorder = [2,1]
    sol = Solution()
    assert str(sol.buildTree(inorder, postorder)) == ' '.join(str(x) for x in inorder)

    #     1
    #    /
    #   2
    #  /
    # 3
    postorder = [3,2,1]
    inorder = [3,2,1]
    sol = Solution()
    assert str(sol.buildTree(inorder, postorder)) == ' '.join(str(x) for x in inorder)
        