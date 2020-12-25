import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if K == 0:
            for s, d, w in flights:
                if s == src and d == dst:
                    return w
            return -1


        answer = 0
        while K != 0:
            for s, d, w in flights[::]:
                if s == src:
                    src = d
                    answer += w
                    K -= 1
                    if src == dst:
                        return answer
                    flights.remove([s,d,w])
                    break
            K -= 1

        return -1

print(Solution().findCheapestPrice(5, [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]], 0, 4, 1))
print(Solution().findCheapestPrice(3, [[0,1,100], [1,2,100], [0,2,500]], 0, 2, 1))