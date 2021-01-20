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
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        elif len(nums) == k:
            max(nums)

        i, l = 0, len(nums)
        answer = []
        while i+k <= l:
            # print(nums[i:i+k])
            answer.append(max(nums[i:i+k]))
            i += 1
        return answer

    def book(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i+k]))
        return r

    def book2(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v

            results.append(current_max)

            if current_max == window.popleft():
                current_max = float('inf')

        return results

            
        


print(Solution().maxSlidingWindow(
    [1, 3, -1, -3, 5, 3, 6, 7], 3
))  # [3,3,5,5,6,7]
print(Solution().maxSlidingWindow(
    [1], 1
))
print(Solution().maxSlidingWindow(
    [1,-1], 1
))
print(Solution().maxSlidingWindow(
    [9, 11], 2
))
print(Solution().maxSlidingWindow(
    [4,-2], 2
))

