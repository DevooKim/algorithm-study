import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

#문제가 뭔소리냐
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #dfs circuit

        graph = collections.defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()

        def dfs(i):
            if i in traced:
                return False
            
            traced.add(i)

            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
        
            return True

        for x in list(graph):
            if not dfs(x):
                return False
        return True


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False
            
            if i in visited:
                return True

            traced.add(i)

            for y in graph[i]:
                if not dfs(y):
                    return False

            traced.remove(i)
            visited.add(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True

a = Solution()