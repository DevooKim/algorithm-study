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
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 무족권 JFK에서 출발한다.

        # for a,b in tickets[::]:
        #     if 'JFK' == a:
        #         result.append(b)
        #         tickets.remove([a, b])
        #         break
        #
        # for a,b in tickets[::]:
        #     if result[-1] == a:
        #         result.append(b)
        #         tickets.remove[a, b]
        #         break

        tickets.sort()
        result = ['JFK']

        def recur(start):
            if not tickets:
                return

            for a, b in tickets[::]:
                if start == a:
                    result.append(b)
                    tickets.remove([a, b])
                    break

            recur(result[-1])

        recur(result[0])

        return result

    def book_default(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')
        return route[::-1]

    def book_stack(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True)
            graph[a].append(b)

        route = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')
        return route[::-1]

    def book_iter(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]

print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
