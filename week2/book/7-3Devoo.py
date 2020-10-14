import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: #중복 제거
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                calc = nums[i] + nums[left] + nums[right]
                if calc < 0:
                    left += 1
                elif calc == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:  #좌우에 같은 수가 있는 경우 건너 뛰기 예시: [-2,*1,*1,*1,0,2,3,4,5,1]
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                else:
                    right -= 1
        return result

a = Solution()
print(a.threeSum([-1,0,1,2,-1,-4]))
