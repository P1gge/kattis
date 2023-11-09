N = int(input())

ord = []

for _ in range(N):
    x = input()
    ord.append(x)
for _ in range(N):
    x = ord.pop()
    print(x)