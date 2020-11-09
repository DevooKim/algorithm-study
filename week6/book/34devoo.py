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
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backTracking(n, discovered):
            if len(n) == len(discovered):
                answer.append(discovered)
                return
            
            for i in n:
                if i not in discovered:
                    discovered.append(i)
                    backTracking(n, discovered)

        answer = []
        for i in nums:
            backTracking(nums, [i])

        return answer

a = Solution()
print(a.permute([1,2,3]))