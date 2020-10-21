import collections

def my():
    def moveLeft(d, count):
        tmp = d.popleft()
        d.append(tmp)
        count += 1
        return d, count

    def moveRight(d, count):
        tmp = d.pop()
        d.appendleft(tmp)
        count += 1
        return d, count

    m, n = map(int, input().split())
    index = list(map(int, input().split()))
    d = collections.deque([i for i in range(1, m+1)])
    count = 0
    for i in index:
        while not (d[0] == i):
            if d.index(i) <= len(d) // 2:
                d, count = moveLeft(d, count)
            else:
                d, count = moveRight(d, count)
        d.popleft()

    print(count)
        
def good():
    n, m = map(int, input().split())
    index = list(map(int, input().split()))
    d = [i for i in range(1, n+1)]

    count = 0

    for i in index:
        p = d.index(i)
        count += min(len(d[p:]), len(d[:p]))
        d = d[p+1:] + d[:p]
    print(count)