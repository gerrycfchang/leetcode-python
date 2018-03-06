# 331. Verify Preorder Serialization of a Binary Tree

# One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. 
# If it is a null node, we record using a sentinel value such as #.# 
# 
#      _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
# For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
# 
# Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without # reconstructing the tree.# 
# 
# Each comma separated value in the string must be either an integer or a character '#' representing null pointer.
# 
# You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".
# 
# Example 1:
# "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Return true


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = preorder.split(',')        
        cnt = 0
        for i in range(len(stack) - 1):
            if stack[i].isdigit():
                cnt += 1
            else:
                if cnt == 0:
                    return False
                cnt -= 1
        return cnt == 0 and stack[-1] == '#'

        
        
if __name__ == '__main__':
    sol = Solution()
    assert sol.isValidSerialization('9,3,4,#,#,1,#,#,2,#,6,#,#') == True
    assert sol.isValidSerialization('1,#') == False
    assert sol.isValidSerialization('9,#,#,1') == False
    assert sol.isValidSerialization('9,2,#,#,#') == True
    assert sol.isValidSerialization('1,#,#,#,#') == False
    assert sol.isValidSerialization('#,#,3,5,#') == False
    assert sol.isValidSerialization('#') == True