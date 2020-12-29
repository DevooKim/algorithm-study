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
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in flights:
      graph[u].append((v, w))  

    #큐: (가중치, 정점, 경유 횟수)
    Q = [(0, src, 0)]

    while Q:
      print(Q)
      cost, node, k = heapq.heappop(Q)

      if node == dst:
        return cost

      if k <= K:
        k += 1
        for v, w in graph[node]:
          alt = cost + w
          heapq.heappush(Q, (alt, v, k))

    return -1

a = Solution()
print(a.findCheapestPrice(3, [[0,1,100], [1,2,100], [0,2,500]], 0, 2, 0))