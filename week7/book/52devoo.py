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
    #내풀이: 브루트포스
    value = 0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def traverse(node):
            if node:
                if low <= node.val <= high:
                    self.value += node.val
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return self.value

    def book(self, root, low, high):
        def dfs(node):
            if not node:
                return 0

            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)

            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)



        
a = Solution()