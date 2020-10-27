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
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        for i, front in enumerate(T):
            for j, back in enumerate(T[i+1:]):
                if front < back:
                    result[i] = j  + 1
                    break
        return result



Solution().dailyTemperatures([73,74,75,71,69,72,76,73])

