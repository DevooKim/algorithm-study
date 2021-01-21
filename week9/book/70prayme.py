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
    def singleNumber(self, nums: List[int]) -> int:
        result = 0 
        # 0 0000 ^ 2 0010
        # 2 0010 ^ 1 0001
        # 3 0011 ^ 2 0010
        # 1 0001
        
        for num in nums:
            result ^= num
        
        return result
    
    def singleNumber2(self, nums: List[int]) -> int:
        a = collections.Counter(nums)
        return a.most_common(len(a))[len(a)-1][0]
        
print(Solution().singleNumber2([4,1,2,1,2]))