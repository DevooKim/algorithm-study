import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

#못풀음
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        queue = collections.deque([root])
        lDepth = 0
        rDepth = 0
        while queue:

            for _ in range(len(queue)):
                cur_root = queue.popleft()

                if cur_root.left:
                    queue.append(cur_root.left)
                    lDepth += 1
                if cur_root.right:
                    queue.append(cur_root.right)
                    rDepth += 1

        return lDepth + rDepth - 1

    logest: int = 0

    def treeDFS(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)

            self.logest = max(self.longest, left + right + 2)

            return max(left, right) + 1

        dfs(root)
        return self.longest

a = Solution()