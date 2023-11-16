N = int(input())

S = 0

while True:
    if N >= 111111111:
        N -= 111111111
        S += 1
    elif N >= 11111111:
        N -= 11111111
        S += 1
    elif N >= 1111111:
        N -= 1111111
        S += 1
    elif N >= 111111:
        N -= 111111
        S += 1
    elif N >= 11111:
        N -= 11111
        S += 1
    elif N >= 1111:
        N -= 1111
        S += 1
    elif N >= 111:
        N -= 111
        S += 1
    elif N >= 11:
        N -= 11
        S += 1
    elif N >= 1:
        N -= 1
        S += 1
    elif N == 0:
        break

print(S)