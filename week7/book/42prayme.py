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

            print(f'DEPTH: {depth}, VALUE: {child.val}')
            a.append(depth)

        search(root, 1)
        return max(a)

    def book(self, root: TreeNode) -> int:
        # 깊이는 어떻게 측정할 수 있을까?
        # DFS는 스택, BFS는 큐를 사용하여 구현
        # 이번 문제는 BFS로 구현
        
        if not root:
            return 0
        
        # 트리 자체를 리스트로 넣음
        queue = collections.deque([root])
        print(queue)
        depth = 0

        while queue:
            depth += 1
            # 큐 연산 추출 노드의 자식 노드 삽입
            for _ in range(len(queue)):
                # 트리 자체를 pop 시킨 후 자식이 있는지 확인함
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
            
        return depth
        



        


print(Solution().maxDepth(TreeNode(val=3, left=TreeNode(9, None, None), right=TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))))
print(Solution().book(TreeNode(val=3, left=TreeNode(9, None, None), right=TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))))