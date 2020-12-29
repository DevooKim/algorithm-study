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
    _min = sys.maxsize
    prev = -sys.maxsize
    def minDiffInBST(self, root: TreeNode) -> int:
        
        def inorder(node):
            if node.left:
                inorder(node.left)

            self._min = min(self._min, node.val - self.prev)
            self.prev = node.val

            if node.right:
                inorder(node.right)

        return self._min

        

a = Solution()