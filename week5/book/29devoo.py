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
        freq = {}
        count = 0

        for char in S:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        for char in J:
            if char in freq:
                count += freq[char]
        return count
        
    def defaultDict(self, J: str, S: str) -> int:
        freq = collections.defaultdict(int)
        count = 0

        for char in S:
            freq[char] += 1

        for char in J:
            count += freq[char]
        
        return count

    def wow(self, J: str, S: str) -> int:
        return sum(s in J for s in S)


            
a = Solution()
print(a.numJewelsInStones("aA", "aAABBBB"))
print(a.hashTable("aA", "aAABBBB"))
print(a.defaultDict("aA", "aAABBBB"))