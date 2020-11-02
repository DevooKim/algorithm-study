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
        p = re.compile('\w')
        J = p.findall(J)
        S = p.findall(S)

        for j in J:
            result += S.count(j)
        return result
        


a = Solution()
print(a.numJewelsInStones("aA", "aAABBBB"))