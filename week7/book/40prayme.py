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
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # (u, v, w) u: 출발노드 v: 도착노드 w: 소요시간
        # N은 노드의 개수
        # K는 출발지

        start = collections.deque()
        start.append(K)
        result = 0
        while times and start:
            start_node = start.popleft()
            for u, v, w in times[::]:
                if u == start_node:
                    start.append(v)
                    result += w
                    times.remove([u, v, w])

        return result

    def networkDelayTime2(self, times: List[List[int]], N: int, K: int) -> int:

        start, end = collections.deque(), collections.deque()
        start.append(K)

        while start:
            start_node = start.popleft()



        result = 0
        while times and start:
            start_node = start.popleft()
            end.append(start_node)
            waste = 0
            for u, v, w in times[::]:
                if start_node == u:
                    start.append(v)
                    waste = w
                    times.remove([u, v, w])
            result += waste

        if not times and start:
            return -1

        return result

    def dijkstra(self, times: List[List[int]], N: int, K: int) -> int:
        # 두 가지를 판별한다.
        # 1. 모든 노드가 신호를 받는 데 걸리는 시간
        # 2. 모든 노드에 도달할 수 있는지 여부
        # A. 다익스트라로 최단시간을 추출해보자
        # B. 모든 노드에 도달할 수 있는지 여부를 노드에 다익스트라 알고리즘 계산 값이 존재하는지로 체크
        graph = collections.defaultdict(list)
        # u, v, w
        # u : { [v1, w1]. [ v2, w2] }
        for u, v, w in times:
            graph[u].appen((v,w))

        Q = [(0, K)]
        dist = collections.defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        if len(dist) == N:
            return max(dist.values())
        return -1



print(Solution().networkDelayTime2([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # 2
