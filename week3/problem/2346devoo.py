n = int(input())
l = list(map(int, input().split()))

i = 0
tmp = l
p = []
for _ in range(len(l)):
    p.append(tmp[i])
    tmp.pop(i)
    
    if tmp[i] > 0:
        i = (i + tmp[i]) % len(tmp)
    else:
        i = abs(i + tmp[i]) % len(tmp)
print(p)
