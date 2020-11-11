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
    def letterCombinations(self, digits: str) -> List[str]:
        count = [0]
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in letters[digits[i]]:
                    count[0] += 1
                    dfs(i + 1, path + j)

        if not digits:
            return []

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        dfs(0, "")
        print(f'COUNT: {count[0]}')
        return result

    def retry(self, digits: str) -> List[str]:
        count = [0]
        letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        result = []
        def dfs(letter, num):
            if len(num) == len(digits):
                result.append(num)
                return

            for char in letters[letter[0]]:
                count[0] += 1
                dfs(letter[1:], num + char)

        dfs(digits, "")
        print(f'COUNT: {count[0]}')
        return result


print(Solution().retry("23"))
Solution().retry("23456789")
print(Solution().letterCombinations("23"))
Solution().letterCombinations("23456789")
# print(Solution().retry(""))
# print(Solution().retry("2"))
# print(Solution().letterCombinations(""))
# print(Solution().letterCombinations("2"))
