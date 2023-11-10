N = int(input())

I = input()

numbers = [int(num) for num in I.split()]

tot = 0

for i in range(N):
    tot += numbers[i]

print(tot)