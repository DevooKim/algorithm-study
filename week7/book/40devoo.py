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

    result = []

    def bfs(node, time):
      print(graph)
      if not graph[node]:
        result.append(time)

      now = graph.pop(node)

      for n in now:
        bfs(n[0], time + n[1])
    
    if not graph[K]:
      return -1
    
    bfs(K, 0)
    return max(result)

  def dijkstra(self, times: List[List[int]], N: int, K: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in times:
      graph[u].append((v, w))
    
    #우선순위 큐: (소요시간, 정점)
    Q = [(0, K)]
    dist = collections.defaultdict(int)

    while Q:
      print(Q, dist)
      time, node = heapq.heappop(Q)
      if node not in dist:
        dist[node] = time

        for v, w in graph[node]:
          alt = time + w
          heapq.heappush(Q, (alt, v))

    if len(dist) == N:
      print(dist)
      return max(dist.values())
    return -1
      
    

a = Solution()
print(a.dijkstra([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
# print(a.networkDelayTime([[1,2,1],[2,1,3]], 2, 2))
