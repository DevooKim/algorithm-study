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


    def bstToGst(self, root: TreeNode) -> TreeNode:
        # right -> root -> left
        #1. 루트 기준 오른쪽 서브트리의 최하위을 찾는다. => root의 마지막
        #2. node -> root -> left순서로 더해간다.
        #3. root가 없으면(root에 도달하면) 다시 오른쪽 끝을 찾는다.(루트 기준 왼쪽 서브트리의 최하위 오른쪽(왼쪽))
        #---------------------------------------------------------------------------------------------
        #1. 이진트리로 바꾼다.
        #2. 뒤에서부터 더한다.

        dq = collections.deque(root.val)
        def treeToList(tree):
            if tree.left:
                dq.appendleft(tree.left.val)
                treeToList(tree.left)
            if tree.right:
                dq.append(tree.right.val)
                treeToList(tree.right)

        #result = collections.deque
        treeToList(root)
        print(dq)

    val: int = 0
    def book(self, root: TreeNode) -> TreeNode:
        if root:
            self.book(root.right)
            self.val += root.val
            root.val = self.val
            self.book(root.left)

        return root
    



a = Solution()