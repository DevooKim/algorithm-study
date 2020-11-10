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
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(length):
            if length == len(nums):
                result.append(nums)
                return

            start, end = 0, 0
            while start + length <= len(nums):
                result.append(nums[start:end + length])
                if end + length == len(nums):
                    start, end = start + 1, 0
                else:
                    end += 1

            dfs(length + 1)

        dfs(1)
        return result

    def book(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):

            result.append(path)
            print(result)
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return result

# print(Solution().subsets([1, 2, 3]))
print(Solution().book([1, 2, 3]))
