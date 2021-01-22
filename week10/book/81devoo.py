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
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #[fuel, count]
        fuel = [[0] * 2 for _ in range(len(gas))] 
        l = len(gas)
        for i in range(l*2):
            idx = i % l
            for start in range(l):
                if start > idx and i < l:
                    break
                if fuel[start][0] >= 0 and fuel[start][1] < len(gas):
                    fuel[start][0] += gas[idx] - cost[idx]
                    fuel[start][1] += 1

                if fuel[start][0] < 0:
                    fuel[start][1] = len(gas)
                start += 1
                
        for idx, f in enumerate(fuel):
            if f[0] >= 0:
                return idx
        return -1

    def book(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]

        return start

a = Solution()
print(a.canCompleteCircuit( [1,2,3,4,5], [3,4,5,1,2]))
# print(a.canCompleteCircuit( [2,3,4], [3,4,3]))