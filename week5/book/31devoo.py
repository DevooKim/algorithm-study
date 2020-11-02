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
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        result = []
        for n in nums:
            if n not in hash:
                hash[n] = 1
            else:
                hash[n] += 1
            # if hash[n] == k:
            #     result.append(n)
        hash = sorted(hash.items(), key=lambda x: x[1])
        for _ in range(k):
            result.append(hash.pop()[0])
        return result

    def counter(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        print(freq)
        freq_heap = []

        for f in freq:
            heapq.heappush(freq_heap, (-freq[f], f))
        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freq_heap)[1])
        return topk
a = Solution()
#print(a.topKFrequent([1,1,1,2,2,3], 2))
# print(a.topKFrequent([1,2], 2))
#print(a.topKFrequent([1,2,2,3], 2))
print(a.counter([1,1,1,2,2,3], 3))
# print(a.counter([1,2], 2))