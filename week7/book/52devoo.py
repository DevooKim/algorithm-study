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

a = Solution()