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
        # max 보다 작은게 나타날 때마다 거래 체결

        buy = float('inf')
        pre = []
        answer = 0
        for i in prices:
            if buy < i and pre:
                answer += i - buy
            buy = i

            pre.append(i)
        return answer




print(Solution().maxProfit([7,1,5,3,6,4]))