X = int(input())
M = int(input())

for i in range(X-1):
    N = int(input())
    if N > M:
        print("Better")
    elif N < M:
        print("Worse")
    else:
        print("Equal")