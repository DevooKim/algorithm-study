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
    root_value: int = sys.maxsize
    path: int = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        # 부모노드부터 자식노드까지 체크하기

    
        # 부모 노드의 val 확인하기
        def dfs(root: TreeNode):
            if not root:
                return

            
            # 왼쪽, 오른쪽 모두 순회한 후에
            # 값 같으면 path + 1

            # path 초기화, 
            # 다음 노드로 이동 후 root_value 초기화


            if self.root_value == root.val:
                path += 1
                dfs(root.left)
                dfs(root.right)

            
            dfs(root.left)
            dfs(root.right)

        self.root_value = root.val
        dfs(root)

        return 1

print(Solution().longestUnivaluePath(TreeNode(5, TreeNode(4, TreeNode(1, None, None), TreeNode(1, None, None)) , TreeNode(5, None, TreeNode(5, None, None)))))
print(Solution().longestUnivaluePath(TreeNode(1, TreeNode(4, TreeNode(4, None, None), TreeNode(4, None, None)), TreeNode(5, None, TreeNode(5, None, None)))))