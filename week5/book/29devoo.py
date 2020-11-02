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
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0

        for j in J:
            result += S.count(j)
        return result

    def hashTable(self, J: str, S: str) -> int:
        h = {}
        count = 0

        for s in S:
            if s not in h:
                h[s] = 1
            else:
                h[s] += 1

        for j in J:
            if j in h:
                count += h[j]
        return count
        


a = Solution()
print(a.numJewelsInStones("aA", "aAABBBB"))
print(a.hashTable("aA", "aAABBBB"))