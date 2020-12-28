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
        count = 0
        while Q:
            time, node = heapq.heappop(Q)
            if node == dst:
                return time
            if node not in dist:
                dist[node] = time

                for v, w in graph[node]:
                    if count > K+1:
                        break
                    alt = w + time
                    heapq.heappush(Q, (alt, v))
                    count += 1
            else:
                count = 0

        return -1


    def book(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        #큐: (가격, 정점, 남은 가능 경유지 수)
        Q = [(0, src, K)]

        while Q:
            print(Q)
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))
        return -1
    

a = Solution()
#print(a.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))
print(a.book(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))