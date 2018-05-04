# 450. Delete Node in a BST
# 
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
# Return the root node reference (possibly updated) of the BST.
# 
# Basically, the deletion can be divided into two stages:
# 
# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).
# 
# Example:
# 
# root = [5,3,6,2,4,null,7]
# key = 3
# 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# 
# Given key to delete is 3. So we find the node with value 3 and delete it.
# 
# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
# 
#     5
#    / \
#   4   6
#  /     \
# 2       7
# 
# Another valid answer is [5,2,6,null,4,null,7].
# 
#     5
#    / \
#   2   6
#    \   \
#     4   7

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.seqlist = []

    def __str__(self):
        del self.seqlist[::]
        self.inorder(self)
        return ''.join(str(x) for x in self.seqlist)

    def inorder(self, curr):
        if not curr: return
        self.inorder(curr.left)
        self.seqlist.append(curr.val)
        self.inorder(curr.right)

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: 
            return root

        if root.val > key: # if key value is less than root value, find the node in the left subtree
            root.left = self.deleteNode(root.left, key)
        elif root.val < key: # if key value is greater than root value, find the node in right subtree
            root.right= self.deleteNode(root.right, key)
        else: #if we found the node (root.value == key), start to delete it
            if not root.right: # if it doesn't have right children, we delete the node then new root would be root.left
                return root.left
            if not root.left: # if it has no left children, we delete the node then new root would be root.right
                return root.right
                # if the node have both left and right children,  we replace its value with the minmimum value in the right subtree and then delete that minimum node in the right subtree
            temp = root.right
            mini = temp.val
            while temp.left:
                temp = temp.left
                mini = temp.val
            root.val = mini # replace value
            root.right = self.deleteNode(root.right,root.val) # delete the minimum node in right subtree
        return root       

if __name__ == '__main__':
    sol = Solution()
    # Test case 1:
    #    5
    #   / \
    #  3   6
    # / \   \
    #2   4   7
    root  = TreeNode(5)
    node1 = TreeNode(3)
    node2 = TreeNode(6)
    node3 = TreeNode(2)
    node4 = TreeNode(4)
    node5 = TreeNode(7)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.right = node5

    #    5
    #   / \
    #  2   6
    #   \   \
    #    4   7
    node = sol.deleteNode(root, 3)
    assert str(node) == '24567'

    #    4
    #   / \
    #  2   6
    #       \
    #        7
    node = sol.deleteNode(root, 5)
    assert str(node) == '2467'

    root = TreeNode(0)
    node = sol.deleteNode(root, 0)
    assert node == None

    root = TreeNode(1)
    node1 = TreeNode(2)
    root.right = node1
    node = sol.deleteNode(root, 2)
    assert str(node) == '1'


    

        