import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

#풀음
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(i, s):
            phone = {
            2: ['a', 'b', 'c'],
            3: ['d','e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
            }
            if len(i) == 0:
                answer.append(s)
                return
            for k in phone[int(i[0])]:
                dfs(i[1:], s+k)

        answer = []
        if len(digits) == 0:
            return answer
        dfs(digits,"")
        
        return answer

a = Solution()
print(a.letterCombinations("23"))
print(a.letterCombinations(""))
print(a.letterCombinations("34"))