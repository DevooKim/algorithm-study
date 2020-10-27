import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

class MyStack:

    def __init__(self):
        self.stack = collections.deque()
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def empty(self) -> bool:
        self.stack = []
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

a = Solution()