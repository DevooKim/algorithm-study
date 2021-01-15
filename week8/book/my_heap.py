import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import List

class BinaryHeap(object):
    def __init__(self):
        # 0번 index를 사용하지 않기 위해서
        # [None]으로 초기화
        self.items = [None]

    # __foo__: python의 매직 메소드 (built-in)
    # 사용: a.__len__()
    def __len__(self):
        return len(self.items) - 1

    def insert(self, k):
        # 1. 요소를 가장 하위 레벨의 최대한 왼쪽으로 삽입한다.
        self.items.append(k)
        # 2~3. 과정이 이루어지는 함수
        self._percolate_up()

        # 시간 복잡도는 O(log n)

    # PEP 8 기준 _ 가 붙으면 내부 함수라는 의미
    # 요소 삽입: Up-Heap
    def _percolate_up(self):
        # 1. 요소를 가장 하위 레벨의 최대한 왼쪽으로 삽입한다.
        # 1. 배열로 표현할 경우 가장 마지막에 삽입한다는 뜻이다.
        # 2. 부모 값과 비교해 값이 더 작은 경우 위치를 변경한다.
        # 3. 계속해서 부모 값과 비교해 위치를 변경한다. 
        # 3. 값이 가장 작을 경우 루트까지 올라간다.
        i = len(self)
        parent = i //2
        while parent >= 0:
            # 부모 노드가 자식 노드보다 크면
            if self.items[i] < self.items[parent]:
                # 부모와 자식을 swap
                self.items[parent], self.items[i] = \
                    self.items[i], self.items[parent]
            
            # index들 조정
            # 반복해서 최대 루트까지 올라갈 수 있다.
            i = parent
            parent = i // 2

    # 추출 Down-Heap
    def extract(self):
        # 루트를 리턴하기 위해서 변수에 저장
        extracted = self.items[1]
        # 맨 마지막 노드를 루트로 옮긴 후
        self.items[1] = self.items[len(self)]
        # 맨 마지막 노드를 버린다
        self.items.pop()
        # 맨 마지막 노드 였던 녀석의 위치를 찾는다
        self._percolate_down(1)
        return extracted

    def _percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left
        
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != idx:
            self.items[idx], self.items[smallest] = \
                self.items[smallest], self.items[idx]
            self._percolate_down(smallest)
        





    
