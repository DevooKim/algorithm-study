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
  def maxDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    result = []
    def rec(tree, depth):
      if tree.left is None and tree.right is None:
        result.append(depth)
        return
      
      if tree.left:
        rec(tree.left, depth+1)
      if tree.right:
        rec(tree.right, depth+1)

    rec(root, 0)
    return max(result) + 1
    
a = Solution()