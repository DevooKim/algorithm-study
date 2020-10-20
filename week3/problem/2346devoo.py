n = int(input())
l = list(map(int, input().split()))

i = -1
tmp = l
p = []
for _ in range(len(l)):
    i += 1
    p.append(tmp[i])
    print(tmp[i])
    tmp.pop(i)
    if tmp[i] < 0:
        i = (i - tmp[i]) % len(tmp)
    else:
        i = (i + tmp[i] - 1) % len(tmp)
print(p)
