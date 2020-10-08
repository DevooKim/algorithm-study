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
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        high = -sys.maxsize - 1
        second_high = 0

        for i in range(len(height) - 1):
            stack.append(height[i])
            high = high < height[i] and height[i] or high
            print(stack, high)

            if len(stack) > 1 and height[i] == high and height[i] > height[i+1]:
                second_high = stack[0] < height[i] and stack[0] or height[-1]
                for j in range(1, len(stack) - 1):
                    water += second_high - stack[j]
                    print(water)
                stack = [height[i]]
        

        return water

a = Solution()
print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))