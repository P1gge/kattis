N = int(input())

les = input()
lek = list(map(int, les.split()))

skip = 0
empty = 0

for i in range(1, N):
    cur = int(lek[i])
    pre = int(lek[i-1])
    if cur > pre:
        skip += abs(pre - cur)
    elif cur < pre:
        empty += abs(pre - cur)
    
print(empty, skip)