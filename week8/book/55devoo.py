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
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        result = 0

        for _ in range(len(nums) - k + 1):
            result = heapq.heappop(nums)

        return result

    def book1(self, nums, k):
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)
        for _ in range(k):
            heapq.heappop(heap)

        return heapq.heappop(heap)

    def book2(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

    def book3(self, nums, k):
        return sorted(nums, reverse=True)[k-1]

    

a = Solution()

print(a.findKthLargest([3,2,1,5,6,4], 2))