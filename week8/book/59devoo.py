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
    def divide(self, arr):
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        left = self.divide(arr[:mid])
        right = self.divide(arr[mid:])

        return self.merged(left, right)

    def merged(self, left, right):
        result = []
        print(left, right)
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                right.pop(0)
        
        if left:
            result+=left
        if right:
            result+=right

        return result

        
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        lists = list(functools.reduce(lambda x, y: x + y, intervals))
        print(self.divide(lists))

    def book(self, intervals: List[List[int]]):
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += [i]
                # merged += i,
        return merged

        
a = Solution()
print(a.book([[1,3],[2,6],[8,10],[15,18]]))