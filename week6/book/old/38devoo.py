import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

#좋다 말음
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if len(tickets) == 1:
            return tickets[0]

        tickets.sort(key= lambda x: x[1])
        discovered = []
        path = []
        def dfs(elements):
            last = discovered[-1]
            next = elements[:]
            if len(elements) == 1:
                path.append(elements[0][0])
                path.append(elements[0][1])
                return

            for e in elements:
                if e[0] == last[1]:
                    discovered.append(e)
                    next.remove(e)
                    path.append(e[0])
                    dfs(next)
                    break

        for t in tickets:
            if t[0] == "JFK":
                path.append("JFK")
                discovered.append(t)
                next = tickets[:]
                next.remove(t)
                dfs(next)
                break
        return path

    def book(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        print(graph)
        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs("JFK")
        return route[::-1]

    def book2(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets):
            graph[a].append(b)
        
        route, stack = [], ["JFK"]
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]
    

a = Solution()
#print(a.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
#print(a.book([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
# print(a.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
# print(a.findItinerary([["JFK","SFO"]]))
#print(a.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
# print(a.book([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))