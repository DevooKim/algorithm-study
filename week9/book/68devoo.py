import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

#투포인터로 풀었음
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -=1
            else:
                return [left+1, right+1]


                

a = Solution()
print(a.twoSum([2,7,8, 10, 11,15], 18))