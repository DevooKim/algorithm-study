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
    def maxSubArray(self, nums: List[int]) -> int:
        window = 1
        answer = float('-inf')
        while window <= len(nums)+1:
            for i in range(0, len(nums)):
                if i+window > len(nums):
                    break
                answer = max(answer,sum(nums[i:i+window]))
            window += 1
        return answer

    def memoization(self, nums: List[int]) -> int:
        # 뒤에서 부터 합한다.
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0

    def kadene(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)

        return best_sum


print(Solution().maxSubArray([-2,-1,-3,4,-1,2,1,-5,4])) #6
print(Solution().maxSubArray([1])) #1
print(Solution().maxSubArray([0])) #0
print(Solution().maxSubArray([-100000])) #-100000