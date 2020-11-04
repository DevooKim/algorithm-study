import collections
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        print(cnt.most_common(k))
        return [answer[0] for answer in cnt.most_common(k)]



print(Solution().topKFrequent([1,1,1,2,2,3], 2))
print(Solution().topKFrequent([1], 1))
print(Solution().topKFrequent([1,2], 2))