N = int(input())
seats = list(input())

available = []
for i in range(N):
    if seats[i] == '.':
        available.append(i)

distance = N - 2
for i in range(len(available)):
    if i > 0:
        distance_new = abs(available[i]-(available[(i-1)]+1))
        if distance_new < distance:
            distance = distance_new
print(distance)