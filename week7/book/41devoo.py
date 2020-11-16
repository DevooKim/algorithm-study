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
        
        Q = [(0, src)]
        dist = collections.defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            count = 0
            print(dist)
            if node not in dist:
                dist[node] = time

                for v, w in graph[node]:

                    alt = w + time
                    heapq.heappush(Q, (alt, v))
                    count += 1
        return min(dist.values())

a = Solution()
print(a.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))