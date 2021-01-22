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
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        #1. [a,b]에서 a, b순서로 정렬
        #2. 하나씩 추출해서 조건이 맞으면 결과에 저장
        #3. people이 남았는데 조건에 맞는 것이 없다면 결과에서 하나를 빼고 다시 반복

        people = collections.deque(sorted(people, key=lambda x: (x[0], x[1])))
        print(people)
        result = []
        # while people:
        #     front = 0
        #     p = people.popleft()
        #     for r in result:
        #         if r[0] >= p[0]:
        #             front += 1
        #     if p[1] == front:
        #         result.append(p)
        #     else:
        #         people.append(p)
    
    def book1(self, people):
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
        
        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result
    

a = Solution()
print(a.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))