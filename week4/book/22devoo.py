import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *
import time

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        start = time.time()
        result = []
        r = 0
        for i, t in enumerate(T):
            L = T[i:]
            count = 0
            for l in L:     #이부분에서 시간 소요: 책에서 처럼 index를 이용하면 간소화 가능
                r += 1
                if t < l:
                    break
                else:
                    count += 1
            if count == len(L):
                count = 0
            result.append(count)
        print(f'my: {time.time() - start}')
        print(f'반복횟수: {r}')
        return result

    def stackSolution(self, T: List[int]) -> List[int]:
        start = time.time()
        answer = [0] * len(T)
        stack = []
        r, r2 = 0, 0
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                print(stack, answer)
                r += 1
                last = stack.pop()
                answer[last] = i - last
            r2 += 1
            stack.append(i)
        print(f'book: {time.time() - start}')
        print(f'반복횟수: {r + r2}')
        return answer

a = Solution()

#print(a.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73, 72, 76, 73, 72, 76, 73, 72, 76, 73, 72, 76, 73, 72, 76, 73, 72, 76, 73, 72, 76, 73]))
#print(a.stackSolution([73, 74, 75, 71, 69, 72, 76, 73, 72, 76, 73, 72, 76, 73, 72, 76, 73, 72, 76, 73, 72, 76, 73, 72, 76, 73, 72, 76, 73]))
print(a.stackSolution([10,9,8,7,6,11,5,4,3,2,1,11]))

#연산 횟수: 내풀이152번, 책49번

#my: 1.4972984790802002
#book: 0.00183868408203125