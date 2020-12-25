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
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        a = []
        def search(child: TreeNode, depth: int) -> int:
            if child.left != None:
                search(child.left, depth+1)
            
            if child.right != None:
                search(child.right, depth+1)

        
            a.append(depth)
        search(root, 1)
        return max(a)


print(Solution().maxDepth(TreeNode(val=3, left=TreeNode(9, None, None), right=TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))))