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
    def majorityElement(self, nums: List[int]) -> int:
        # 1. Counter
        # 2. 분할 -> 딕셔너리에 카운팅

        counter = collections.defaultdict(int)
        result = []

        def divide(arr):
            if len(arr) < 2:
                return arr
            
            mid = len(arr) // 2
            L = divide(arr[:mid])
            R = divide(arr[mid:])
            
            if L:
                counter[L[0]] += 1
            if R:
                counter[R[0]] += 1

        divide(nums)
        for c in counter:
            if counter[c] > len(nums) // 2:
                result.append(c)

        return result
a = Solution()
print(a.majorityElement([2,2,1,1,1,2,2]))