N = int(input())
match = input()

A_point, B_point = 0, 0
A, B = 0, 0

for i in match:
    if i == 'A':
        A_point += 1
    else:
        B_point += 1

    if (A + B) >= 2:
        if A_point >= 15 and (A_point - B_point) >= 2:
            A += 1
            A_point, B_point = 0, 0
        elif B_point >= 15 and (B_point - A_point) >= 2:
            B += 1
            A_point, B_point = 0, 0
    else:
        if A_point >= 25 and (A_point - B_point) >= 2:
            A += 1
            A_point, B_point = 0, 0
        elif B_point >= 25 and (B_point - A_point) >= 2:
            B += 1
            A_point, B_point = 0, 0

print(A, B)