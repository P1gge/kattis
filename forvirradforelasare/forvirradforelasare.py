N = int(input())

les = list(map(int, input().split()))

skip = 0
empty = 0

for i in range(1, N):
    cur = int(les[i])
    pre = int(les[i-1])
    if cur > pre:
        skip += abs(pre - cur)
    elif cur < pre:
        empty += abs(pre - cur)
    
print(empty, skip)