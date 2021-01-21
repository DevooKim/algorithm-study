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
        buy, profit = -1, 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1] and buy == -1:
                buy = prices[i]
            elif prices[i] > prices[i+1] and buy != -1:
                profit += (prices[i] - buy)
                buy = -1
        if buy != -1:
            profit += (prices[-1] - buy)
        return profit
a = Solution()
# print(a.maxProfit([7,1,5,3,6,4]))
print(a.maxProfit([1,2,3,4,5]))