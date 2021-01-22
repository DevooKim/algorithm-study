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
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count(1)        

a = Solution()