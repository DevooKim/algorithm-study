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
        queue = collections.deque([root])
        result = TreeNode(root.val)
        while queue:
            for _ in len(queue):
                cur_root = queue.popleft()

                if cur_root.left:
                    queue.append(cur_root.right)
                if cur_root.right:
                    queue.append(cur_root.left)
        return root

a = Solution()