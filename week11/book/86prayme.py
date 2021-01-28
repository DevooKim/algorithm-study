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

print(Solution().maxSubArray([-2,-1,-3,4,-1,2,1,-5,4])) #6
print(Solution().maxSubArray([1])) #1
print(Solution().maxSubArray([0])) #0
print(Solution().maxSubArray([-100000])) #-100000