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
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 우선순위 = 최소 최대값을 추출할 수 있다.
        # 그리디에 잘 어울린다
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])

        return result

print(Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))