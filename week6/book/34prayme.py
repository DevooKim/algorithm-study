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
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(lists):
            if len(result) == target_length:
                return
            print(f'LISTS: {lists}')
            result.append(lists)
            head = lists[:1]
            tail = lists[1:]
            for i in range(len(lists[1:]) - 1):
                tail = tail[1:] + tail[:1]
                result.append(head + tail)
            print(f'HEAD: {head}')
            print(f'TAIL: {tail}')
            print(f'TAIL + HEAD: {tail + head}')
            dfs(lists[1:] + lists[:1])

        target_length = 1
        for i in range(2, len(nums) + 1):
            target_length *= i

        result = []
        dfs(nums)

        return result


print(Solution().permute([1, 2, 3]))

# [[5, 4, 6, 2], [5, 6, 2, 4], [5, 2, 4, 6], [4, 6, 2, 5], [4, 2, 5, 6], [4, 5, 6, 2], [6, 2, 5, 4], [6, 5, 4, 2],
#  [6, 4, 2, 5], [2, 5, 4, 6], [2, 4, 6, 5], [2, 6, 5, 4], [5, 4, 6, 2], [5, 6, 2, 4], [5, 2, 4, 6], [4, 6, 2, 5],
#  [4, 2, 5, 6], [4, 5, 6, 2], [6, 2, 5, 4], [6, 5, 4, 2], [6, 4, 2, 5], [2, 5, 4, 6], [2, 4, 6, 5], [2, 6, 5, 4]]
# #
# [[5, 4, 6, 2], [5, 4, 2, 6], [5, 6, 4, 2], [5, 6, 2, 4], [5, 2, 4, 6], [5, 2, 6, 4], [4, 5, 6, 2], [4, 5, 2, 6],
#  [4, 6, 5, 2], [4, 6, 2, 5], [4, 2, 5, 6], [4, 2, 6, 5], [6, 5, 4, 2], [6, 5, 2, 4], [6, 4, 5, 2], [6, 4, 2, 5],
#  [6, 2, 5, 4], [6, 2, 4, 5], [2, 5, 4, 6], [2, 5, 6, 4], [2, 4, 5, 6], [2, 4, 6, 5], [2, 6, 5, 4], [2, 6, 4, 5]]