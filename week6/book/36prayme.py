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
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1.candidates가 큰가?
        # 2.1 %가 0인가? yes -> // 후 갯수 리턴
        # 2.2 %가 0인가? no -> // 갯수 추가 후
        # 2.2 % 후 남은 숫자를 다시 1. 실행
        # 중복은 제거!
        # 가장 큰 수부터 하면 중복 없을듯

        result = []
        # [2, 3, 6, 7], 7
        def func(candidate, num):
            if sum(candidate) > num:
                return

            print(f'CANDIDATE: {candidate}')

            clone = candidate[::-1]
            for i in candidate[::-1]:
                element = [i] * (target // i)
                clone.remove(i)
                func(clone, num % i)

        def book(self, candidates: List[int], target: int) -> List[List[int]]:
            result = []

            def dfs(csum, index, path):
                if csum < 0:
                    return
                if csum == 0:
                    result.append(path)
                    return

                for i in range(index, len(candidates)):
                    dfs(csum - candidates[i], i, path + [candidates[i]])

            dfs(target, 0, [])
            return result

        return result




print(Solution().combinationSum([2,3,6,7], 7))
print(Solution().combinationSum([2,3,5], 8))