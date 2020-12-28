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
      
    

a = Solution()
# print(a.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
print(a.networkDelayTime([[1,2,1],[2,1,3]], 2, 2))
