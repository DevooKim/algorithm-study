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
        # left = collections.deque(left)
        # right = collections.deque(right)
        print(left, right)
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                # left.appendleft(right.popleft())
                right.pop(0)
        
        if left:
            result+=left
        if right:
            result+=right
        return result

        
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        lists = list(functools.reduce(lambda x, y: x + y, intervals))
        print(self.divide(lists))

        
a = Solution()
print(a.merge([[1,3],[2,6],[8,10],[15,18]]))