# 173. Binary Search Tree Iterator
#
# Implement an iterator over a binary search tree (BST). 
# 
# Your iterator will be initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, 
#
# where h is the height of the tree.

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.res = []
        self.inorder(root)
        
    def inorder(self, node):
        if not node: return
        self.inorder(node.left)
        self.res.append(node.value)
        self.inorder(node.right)        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.res) > 0             

    def next(self):
        """
        :rtype: int
        """
        return self.res.pop(0)
        
import sys
sys.path.append('../../')
from leetCodeUtil import TreeNode

if __name__ == '__main__':
    root = TreeNode(1)
    i, v = BSTIterator(root), []
    while i.hasNext(): 
        v.append(i.next())
    assert v == [1]