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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, num in nums:
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i