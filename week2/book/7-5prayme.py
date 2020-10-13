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
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if answer < profit:
                    answer = profit
        print(answer)
        return answer

    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit


Solution().maxProfit([7, 1, 5, 3, 6, 4])
