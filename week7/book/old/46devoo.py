import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

#못풀음
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        q1 = collections.deque([t1])
        q2 = collections.deque([t2])

        if len(q1) < len(q2):
            q1, q2 = q2, q1

        while q1 and q2:

            n1 = q1.popleft()
            n2 = q2.popleft()

            if n1 and n2:
                q1.append(n1.val+n2.val)
            elif n1:
                q1.append(n1)
            elif n2:
                q1.append(n2)
        return q1

    def book(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.book(t1.left, t2.left)
            node.right = self.book(t1.left, t2.left)

            return node
        else:
            return t1 or t2
    

a = Solution()