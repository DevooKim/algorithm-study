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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        elem = sorted([nums[i], nums[j], nums[k]])
                        if elem in answer:
                            break
                        answer.append(elem)
        print(f"answer: {answer}")
        return answer


Solution().threeSum([-1, 0, 1, 2, -1, -4])
