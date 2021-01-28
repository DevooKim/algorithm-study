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
    def majorityElement(self, nums: List[int]) -> int:

        return collections.Counter(nums).most_common(1)[0][0]

    def book_dp(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)
            
            if counts[num] > len(nums) // 2:
                return num

    def book_division(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]

    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]

print(Solution().majorityElement([3,2,3]))