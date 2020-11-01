import collections
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)

        answer = []
        for num, freq in cnt.most_common():
            if freq >= k:
                answer.append(num)

        return answer


print(Solution().topKFrequent([1,1,1,2,2,3], 2))
print(Solution().topKFrequent([1], 1))
print(Solution().topKFrequent([1,2], 2))