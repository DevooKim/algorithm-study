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
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()

        for n in nums:
            heapq.heappush(heap, -n)

        print(heap)
        
        for _ in range(k-1):
            heapq.heappop(heap)
            print(heap)
    
        return -heapq.heappop(heap)

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        # 파라미터를 힙 특성을 만족하도록 바꿔주는 함수
        # 값을 하나라도 추가하면 힙 특성이 깨진다.
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        # nums에서 큰 순서대로 k번째까지 추출해준다.
        # 내부적으로 heapify 함수도 호출해준다.
        # nsmallest()도 있다.
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest4(self, nums: List[int], k: int) -> int:
        # 정렬해버리기
        return sorted(nums, reversed=True)[k-1]




print(Solution().findKthLargest([3,2,1,5,6,4], 2))