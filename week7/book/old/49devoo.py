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
    
    #result: [depth, start]
    result = [sys.maxsize,-1]

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)


        def dfs(elements, key, path):
            if not key in elements.keys():
                if self.result[0] > len(path):
                    print(path)
                    self.result = [len(path), path[0]]
                return

            while elements[key]:
                node = elements[key].pop()
                path.append(node)
                next = dict(elements)
                del next[key]
                dfs(next, node, path)

            
        for k in graph.keys():
            dfs(graph, k, [])
        return self.result[1]


    def book(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        leaves = []

        #첫번째 리프노드 추가
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves
    
a = Solution()
print(a.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
print(a.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))