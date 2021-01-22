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
    def dist(self, point):
        return math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2))

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        arr = []
        result = []
        for idx, p in enumerate(points):
            arr.append([self.dist(p), idx])

        arr.sort()
        for i in range(K):
            result.append(points[arr[i][1]])
        return result





    def book(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (dist, x, y))
        
        result = []
        for _ in range(K):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))
        return result
a = Solution()
print(a.kClosest([[1,3], [-2,2]], 1))
print(a.kClosest([[3,3],[5,-1],[-2,4]],2))

#내풀이 : 2n + log(n)
#책풀이 : 2n * log(n)