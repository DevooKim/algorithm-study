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
        # 실패 케이스: [2,3,null,1]
        # 개선방안: 루트를 기준으로 거리를 기록해보자
        # 기준으로 하되 left와 right를 구분지어야한다.
        if not root:
            return 0
 
        a = []
        def search(child: TreeNode, depth: int) -> int:
            if child.left != None:
                search(child.left, depth+1)
            
            if child.right != None:
                search(child.right, depth+1)

            print(f'depth: {depth}, node: {child.val}')
            a.append(depth)
        search(root, 0)
        
        if len(a) == 1:
            return 0
        
        if len(a) == 2:
            return 1
        
        a.pop()
        print(a)
        return max(a) + min(a)
    
    def fix(self, root: TreeNode) -> int:
        # 루트를 기준으로 거리를 기록해보자
        # 기준으로 하되 left와 right를 구분지어야한다.
        if root == None:
            return 0
        # def check_root(self, root: TreeNode) -> int:
        #     if root == None or (root.left == None and root.right == None):
        #         return 0
        

        def search(child: TreeNode, depth: int) -> int:
            if child == None:
                return depth - 1

            print(f'VALUE: {child.val}, DEPTH: {depth}')

            if child.left != None and child.right != None:
                return depth

            print(f'depth: {depth}, node: {child.val}')
            return max(search(child.left, depth+1), search(child.right, depth+1))

        right, left = 0, 0
        try:
            left = search(root.left, 1)
        except NameError:
            print("ROOT.LEFT IS NULL")
        
        try:
            right = search(root.right, 1)
        except NameError:
            print("ROOT.RIGHT IS NULL")


        print(f'LEFT: {left}, RIGHT:{right}')
        return right + left


print(Solution().fix(TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)), TreeNode(3, None, None))))