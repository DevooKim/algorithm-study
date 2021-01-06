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
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(word):
            if len(word) == 1:
                return True

            cnt = 0
            n = len(word) // 2
            while cnt < n:
                if word.popleft() != word.pop():
                    return False
                cnt += 1
            return True
                    
        answer = []
        i = 0
        while i < len(words):
            j = i+1
            while j < len(words):
                word = collections.deque(words[i] + words[j])
                if isPalindrome(word):
                    answer.append((i,j))
                
                word = collections.deque(words[j] + words[i])
                if isPalindrome(word):
                    answer.append((j,i))
                j += 1
            i += 1

        return answer


print(Solution().palindromePairs(['abcd','dcba','lls','s','sssll']))
print(Solution().palindromePairs(['bat','tab','cat']))
print(Solution().palindromePairs(["a","abc","aba",""]))