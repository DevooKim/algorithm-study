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
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        for i in g:
            for j in s:
                if i <= j:
                    count += 1
                    s.remove(j)
                    break

        return count

    #그리디
    def book1(self, g, s):
        g.sort()
        s.sort()

        child_i = cookie_j = 0

        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
        return child_i

    #이진 탐색
    def book2(self, g, s):
        g.sort()
        s.sort()

        result = 0
        for i in s:
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1

        return result

a = Solution()
print(a.findContentChildren([1,2,3],[1,2,4]))