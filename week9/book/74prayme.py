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
    def hammingWeight(self, n: int) -> int:
        MASK = sys.maxsize
        print(n & sys.maxsize)
    
    def book(self, n: int) -> int:
        # return bin(n ^ 0).count('1')
        return bin(n).count('1')
