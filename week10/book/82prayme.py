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
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        heapq.heapify(g)
        heapq.heapify(s)

        answer = 0
        while g and s:
            greedy = heapq.heappop(g)
            while s:
                if greedy <= heapq.heappop(s):
                    answer += 1
                    break
        return answer

    def book(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_i = cookie_j = 0

        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1

        return child_i

# print(Solution().findContentChildren([1,2,3], [1,1]))
# print(Solution().findContentChildren([1,2], [1,2,3]))
print(Solution().findContentChildren([10,9,8,7], [5,6,7,8]))