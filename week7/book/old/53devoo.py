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
    prev = -sys.maxsize
    result = sys.maxsize

    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)    
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result


    def book2(self, root: TreeNode) -> int:
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return result


a = Solution()