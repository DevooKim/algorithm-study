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
    def hammingDistance(self, x: int, y: int) -> int:
        return collections.Counter(bin(x^y)[2:])['1']

    def book_xor(self, x: int, y: int) -> int:
        return bin(x^y).count('1')


print(Solution().hammingDistance(1, 4))