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

a = Solution()
print(a.findContentChildren([1,2,3],[1,2,4]))