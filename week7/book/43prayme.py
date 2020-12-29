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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # depth + depth 방법을 시도해보자
        if not root:
            return 0

        
            
        a = []
        def search(child: TreeNode, depth: int) -> int:
            if child.left != None:
                search(child.left, depth+1)
            
            if child.right != None:
                search(child.right, depth+1)

        
            a.append(depth)
        search(root, 0)
        print(a)
        return max(a) - min(a)


print(Solution().diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)), TreeNode(3, None, None))))