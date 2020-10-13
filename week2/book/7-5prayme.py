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


Solution().maxProfit([7, 1, 5, 3, 6, 4])
