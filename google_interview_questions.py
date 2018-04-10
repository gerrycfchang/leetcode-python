import sys
import collections
sys.path.append('../')
from leetCodeUtil import ListNode
from leetCodeUtil import TreeNode
class Interview(object):
    def normalizeString(self, s):
        string = s.split()
        return ' '.join(string)
    
    def checkPairsIntervalOverlap(self, nums):
        nums.sort(key=lambda x: x[0])
        for i in range(len(nums)-1):
            if nums[i][1]> nums[i+1][0]:
                return True
        return False

    ### First Subarray Sums to Target
    def combination(self, nums, target):
        ret = []
        def dfs(nums, start, target, reslist):            
            if target == 0 and reslist not in ret:
                ret.append(reslist)
                return
            for i in range (start, len(nums)):
                if len(ret) > 0:
                    return
                dfs(nums, i + 1, target - nums[i], reslist + [nums[i]])
        dfs((nums), 0, target, [])
        return ret[0] if len(ret) > 0 else [-1, -1]

    def constructBST(self, head):
        if not head: return None
        
        slow = fast = last = head
        # find out the center of the node
        while fast.next and fast.next.next:
            last = slow
            slow = slow.next
            fast = fast.next.next
        # right is slow
        fast = slow.next
        
        # left part is head
        last.next = None
        cur = TreeNode(slow.val)
        if head != slow:
            cur.left = self.constructBST(head)
        cur.right = self.constructBST(fast)
        return cur

    def isHappyNumber(self, num):
        table, res = [], num
        while not (res in table):
            if res == 1:
                return True
            table.append(res)
            input = res
            res = 0
            while input >0:
                res += (input%10) ** 2
                input /= 10
        return False

    def longestConsecutive(self, root):
        def dfs(node, value,  out, maxLen):
            if not node: return
            if value == node.value:
                out += 1
            else:
                out = 1
            maxLen[0] = max(out, maxLen[0])
            dfs(node.left, node.value, out, maxLen)
            dfs(node.right, node.value, out, maxLen)
        maxLen = [0]
        dfs(root, root.value, 1, maxLen)
        return maxLen[0]  

    def findModeInBST(self, root):
        from collections import Counter
        def inorder(node, c):
            if not node: return
            inorder(node.left, c)
            c[node.value] += 1
            inorder(node.right, c)
        c = Counter()
        inorder(root, c)
        maxnum = max(c.values())
        res = []
        for key, value in c.iteritems():
            if value == maxnum:
                res.append(key)
        return res
    
    def findLIS(self, nums):
        length = len(nums)
        dp = [1 for _ in range(length+1)]
        for i in range(length):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)

    def fib(self, n):
        dp = [0 for i in range (n+1)]
        dp[0], dp[1] = 1, 1
        for i in range (2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def fibRecur(self, n):
        if n == 0 or n == 1: return 1
        return self.fibRecur(n-1) + self.fibRecur(n-2)

    def firstRepeatChar(self, s):
        charset = set()
        for i in range(len(s)):
            if s[i] in charset:
                return s[i]
            else:
                charset.add(s[i])
        return None

    def firstNonRepeatChar(self, s):
        from collections import OrderedDict
        charset = OrderedDict()
        for i in range(len(s)):
            if s[i] not in charset:
                charset[s[i]] = 1
            else:
                charset[s[i]] += 1

        for key, value in charset.items():
            if value == 1:
                return key
        return None

    def longestPalindromSubseq(self, s):
        if len(s) <= 1: return len(s)
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n): dp[i][i] = 1
        for size in range(2,n+1):
            for i in range(n-size+1):
                j = i + size - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][n-1]



if __name__ == '__main__':
    sol = Interview()
    assert sol.normalizeString('  hello  world ') == 'hello world'

    nums = [[1,3],[7,9],[2,6]]
    assert sol.checkPairsIntervalOverlap(nums) == True

    nums = [[1,3],[7,9],[10,16]]
    assert sol.checkPairsIntervalOverlap(nums) == False

    nums=[4, 3, 5, 7, 8]
    exp = sol.combination(nums, 12)
    assert  exp == [4, 3, 5]

    nums=[1, 2, 3, 4]
    exp = sol.combination(nums, 15)
    assert  exp == [-1,-1]

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    result = sol.constructBST(node1)
    res = result.getDFS(result)
    exp1 = [1, 2, 3, 4, 5]
    assert  res == exp1

    assert sol.isHappyNumber(100) == True
    assert sol.isHappyNumber(22) == False

    sample2 = TreeNode(2)
    sample3 = TreeNode(3)
    sample4 = TreeNode(2)
    sample5 = TreeNode(1)
    sample2.right = sample3
    sample3.left = sample4
    sample4.left = sample5
    assert sol.longestConsecutive(sample2) == 2

    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(2)

    root.right = node1
    node1.left = node2        
    assert sol.findModeInBST(root) == [2]

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    assert sol.findLIS(nums) == 4

    assert sol.fib(5) == sol.fibRecur(5)
    assert sol.firstRepeatChar('abca') == 'a'
    assert sol.firstRepeatChar('bcaba') == 'b'
    assert sol.firstRepeatChar('abc') == None
    assert sol.firstRepeatChar('') == None
    assert sol.firstNonRepeatChar('ababcad') == 'c'
    assert sol.firstNonRepeatChar('abcdefg') == 'a'
    assert sol.firstNonRepeatChar('abab') == None
    assert sol.firstNonRepeatChar('') == None
    assert sol.longestPalindromSubseq('bbbab') == 4
 