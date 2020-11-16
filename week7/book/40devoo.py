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
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for t in times:
            graph[t[0]].append(t[1:])

        if not graph[K]:
            return -1

        weight = []
        def bfs(start, elements, w):
            if not elements[start]:
                weight.append(w)
                return
            print(elements, start)
            while elements[start]:
                e = elements[start].pop()
                bfs(e[0], elements, w + e[1])
                
        bfs(K, graph, 0)
        return max(weight)

a = Solution()
print(a.networkDelayTime([[2,3,1],[2,1,1],[3,4,1]], 4, 2))
print(a.networkDelayTime([[1,2,1], [2,1,3]], 2, 2))