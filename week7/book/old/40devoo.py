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

    def dijkstra(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
        print(graph)
        # 큐 변수: [(소요시간, 정점)]
        Q = [(0, K)]
        dist = collections.defaultdict(int)

        while Q:
            #print(Q, dist)
            time, node = heapq.heappop(Q)
            print(dist)
            if node not in dist:
                dist[node] = time

                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
                    print(Q)

        if len(dist) == N:
            return max(dist.values())
        return -1
    

a = Solution()
# print(a.networkDelayTime([[2,3,1],[2,1,1],[3,4,1]], 4, 2))
# print(a.networkDelayTime([[1,2,1], [2,1,3]], 2, 2))
#print(a.dijkstra([[2,3,1],[2,1,1],[3,4,1]], 4, 2))
# print(a.dijkstra([[3,1,5],[3,2,2],[2,1,2],[3,4,1],[4,5,1],[5,6,1],[6,7,1],[7,8,1],[8,1,1]], 8, 3))
print(a.networkDelayTime([[1,2,1],[2,1,3]], 2, 2))
