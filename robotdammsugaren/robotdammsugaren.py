R, C, N = map(int, input().split())
com = input()

room = []
for i in range(R):
    c = input()
    room.append(list(c))

start_x, start_y = None, None
for x in range(R):
    for y in range(C):
        if room[x][y] == "O":
            start_x = x
            start_y = y
            break
    if start_x != None and start_y != None:
        break

for i in com:
    if i == "<":
        while True:
            if (y > 0) and (y <= len(room[x])):
                if room[x][(y - 1)] == ".":
                    y -= 1
                else:
                    break
            else:
                break
    elif i == "^":
        while True:
            if (x > 0) and (x <= len(room)):
                if room[(x - 1)][y] == ".":
                    x -= 1
                else:
                    break
            else:
                break