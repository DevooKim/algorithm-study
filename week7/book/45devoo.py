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
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return

            left = dfs(node.right)
            right = dfs(node.left)
            node.left, node.right = left, right

            return node

        return dfs(root)

    def bfs(self, root: TreeNode) -> TreeNode:
        queue = collections.defaultdict([root])

        while queue:
            node = queue.popleft()

            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root

    def dfs(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()

            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)

        return root
            


        

a = Solution()