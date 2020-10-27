import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.queue = collections.deque(5)
        

    def enQueue(self, value: int) -> bool:

        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()