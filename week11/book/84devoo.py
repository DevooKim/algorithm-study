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
    def calc(self, op):
        if op[1] == '+':
            return op[0] + op[2]
        elif op[1] == '-':
            return op[0] - op[2]
        elif op[1] == '*':
            return op[0] * op[2]

    def diffWaysToCompute(self, input: str) -> List[int]:
        result = []
        def divide(input):
            if len(input) == 1:
                result.append(input)
                return
            if len(input) == 3:
                return input

            half = len(input) // 2

            L = divide(input[:half])
            R = divide(input[half:])

            oL = self.calc(L)
            oR = self.calc(R)

    def book(self, input):
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results

        if input.isdigit():
            return [int(input)]

        results = []
        for index, value in enumerate(input):
            if value in "-+*":
                left = self.book(input[:index])
                right = self.book(input[index + 1:])

                results.extend(compute(left, right, value))
        return results
            


a = Solution()