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

    def book(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root

    def book2(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left #전위 순회

                stack.append(node.left)
                stack.append(node.right)

                #node.left, node.right = node.right, node.left #후위 순회


        return root

    def book3(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.book3(root.right), self.book3(root.left)
        return root
    

a = Solution()