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
    def leastInterval(self, tasks: List[str], n: int) -> int:

        p = collections.defaultdict()
        ts = collections.Counter(tasks)

        remain = list(ts.values())
        ts = ts.keys()

        for k in ts:
            p[k] = 0

        cnt = 0
        answer = 0
        j = 0
        # A, B
        # 3, 3
        # A: 0
        # B: 1
        # cnt = 0 A
        # cnt = 1 B
        # cnt - p["A"] 0
        # cnt = 2 A
        idle = 0
        while remain[0] != 0 or remain[1] != 0:
            for i, k in enumerate(ts):
                if cnt - p[k] <= n:
                    idle += 1
                    continue
                else:
                    remain[i] -= 1
                    p[k] = cnt
                    answer += 1
                cnt += 1
        

        return answer + idle

    def book(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0

            for task, _ in counter.most_common(n+1):
                sub_count += 1
                result += 1

                counter.subtract(task)
                counter += collections.Counter()


            if not counter:
                break

            result += n - sub_count + 1
        return result





print(Solution().leastInterval(["A","A","A","B","B","B"], 2))