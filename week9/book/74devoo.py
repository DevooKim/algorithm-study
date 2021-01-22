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
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

    def book(self, n):
        count = 0
        while n:
            n &= n-1
            count += 1
        return count

a = Solution()