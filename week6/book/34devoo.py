import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

#못 풀음
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

    def book(self, nums: List[int]) -> List[List[int]]:
        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        result = []
        prev_elements = []

        dfs(nums)
        return result

    def book2(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))

a = Solution()
print(a.book([1,2,3]))