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
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        def merge(n1, n2):
            if n1 and n2:
                node = TreeNode(n1.val + n2.val)
                node.left = merge(n1.left, n2.left)
                node.right = merge(n1.right, n2.right)

                return node
            else:
                return n1 or n2

        return merge(t1, t2)
            

a = Solution()