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
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = sys.maxsize

        for i in prices:
            lowest = min(i, lowest)
            profit = max(i - lowest, profit)
        return profit

a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))