import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        return 1

print(Solution().longestUnivaluePath(TreeNode(5, TreeNode(4, TreeNode(1, None, None), TreeNode(1, None, None)) , TreeNode(5, None, TreeNode(5, None, None)))))
print(Solution().longestUnivaluePath(TreeNode(1, TreeNode(4, TreeNode(4, None, None), TreeNode(4, None, None)), TreeNode(5, None, TreeNode(5, None, None)))))