N = int(input())

tot = 0

for i in range(N):
    H, B, K = input().split()
    if int(H) < int(B):
        tot += abs(int(B)-int(H)) * int(K)
        
print(tot)