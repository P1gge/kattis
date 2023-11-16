N = int(input())

U = 100 - N
S = 0

while True:
    if U >= 20:
        U -= 20
        S += 1
    elif U >= 5:
        U -= 5
        S += 1
    elif U >= 1:
        U -= 1
        S += 1
    elif U == 0:
        break

print(S)