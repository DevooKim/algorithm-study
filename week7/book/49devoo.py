import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for i, j in edges:      #무방향성 그래프
            graph[i].append(j)
            graph[j].append(i)

        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)    #말단 노드

        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                neighbor = graph[leaf].pop()    #그래프에서 말단 노드 제거
                graph[neighbor].remove(leaf)    #무방향성 그래프이므로 연결되어있는 노드에서도 제거

                if len(graph[neighbor])  == 1:  #제거 후 말단 노드가 되었다면 leaves에 추가
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves



a = Solution()