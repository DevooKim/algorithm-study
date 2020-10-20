def my():
    n, k = map(int, input().split())

    l = [i for i in range(1, n+1)]
    rtn = []
    prev = 0
    while l:
        prev = (prev + k - 1) % len(l)
        rtn.append(l[prev])
        l = l[:prev] + l[prev+1:]
    s = "<"
    for i in range(len(rtn)):
        if i == len(rtn) - 1:
            s += (str(rtn[i]) + ">")
        else:
            s += (str(rtn[i]) + ", ")
    print(s)

def good():
    n, k = map(int, input().split())

    l = [i for i in range(1, n+1)]
    rtn = []
    prev = 0
    while l:
        prev = (prev + k - 1) % len(l)
        rtn.append(str(l[prev]))
        l.pop(prev)

    print('<', ', '.join(rtn), '>', sep='')