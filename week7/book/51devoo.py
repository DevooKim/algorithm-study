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
    value = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def traverse(node):
            if node:

                traverse(node.right)
                self.value += node.val
                node.val = self.value
                traverse(node.left)

            return node

        return traverse(root)



a = Solution()