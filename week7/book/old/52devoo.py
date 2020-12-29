import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

#풀었음 => 브루드포스

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    result = 0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def recursive(root):
            if root and root.val >= low and root.val <= high:
                self.result += root.val
            
            if root:
                recursive(root.left)
                recursive(root.right)

        recursive(root)
        return self.result

    def book(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0

            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)

            return node.val + dfs(node.left) + dfs(node.right)

    def book2(self, root: TreeNode, low: int, high: int) -> int:
        stack, sum = [root], 0

        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                elif node.val < high:
                    stack.append(node.right)
                
                if low <= node.val <= high:
                    sum += node.val
        return sum

    def book3(self, root: TreeNode, low: int, high: int) -> int:
        stack, sum = [root], 0

        while stack:
            node = stack.pop(0)
            if node:
                if node.val > low:
                    stack.append(node.left)
                elif node.val < high:
                    stack.append(node.right)
                
                if low <= node.val <= high:
                    sum += node.val
        return sum
a = Solution()