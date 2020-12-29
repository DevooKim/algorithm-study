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
  def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    _dict = collections.defaultdict(list)

    for s, e in sorted(tickets, reverse=True):
      _dict[s].append(e)
      
    route = []
    def dfs(a):
      while _dict[a]:
        dfs(_dict[a].pop())
      route.append(a)

    dfs("JFK")
    return route[::-1]

a = Solution()
# print(a.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(a.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))