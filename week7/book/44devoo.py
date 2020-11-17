import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    depth: list = []
    longest: int = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root is None:
            return 0

        def dfs(node: TreeNode) -> int:
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            if node.val == node.left.val or node.val == node.right.val:
                self.longest = max(self.longest, left + right + 2)
            elif node.val == node.left.val:
                self.longest = max(self.longest, left + 1)
            elif node.val == node.right.val:
                self.longest = max(self.longest, right + 1)
            else:
                self.longest = 0

            return max(left, right) + 1

        dfs(root)
        return max(self.depth)

a = Solution()