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
        
        left, right = [0], [0]
        def search_left(root: TreeNode, depth):

            if root.left != None:
                search_left(root.left, depth+1)
            
            if root.right != None:
                search_left(root.right, depth+1)

            print(f"LEFT:: VAL: {root.val}, DEPTH: {depth}")
            left[0] = max(left[0], depth)

        def search_right(root: TreeNode, depth):

            if root.left != None:
                search_right(root.left, depth+1)
            
            if root.right != None:
                search_right(root.right, depth+1)

            print(f"RIGHT:: VAL: {root.val}, DEPTH: {depth}")
            right[0] = max(right[0], depth)
        
        if root.left != None:
            search_left(root.left, 1)
        
        if root.right != None:
            search_right(root.right, 1)

        return left[0] + right[0]
   
    longest: int = 0
    def book_dfs(self, root: TreeNode) -> int:
        # 가장 깊은 노드(리프 노드)까지 탐색한다.
        # 부모로 거슬러 올라가면서 거리를 계산한다.
        # 상태값을 업데이트하면서 누적해나간다.
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            # 상태값
            return max(left, right) + 1

        dfs(root)
        return self.longest

print(Solution().diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)), TreeNode(3, None, None))))