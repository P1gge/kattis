#   Läs in 9 siffror i A[1...9]
#   Låt summa = 0
#   För varje siffra s = A[1], A[3], A[5], A[7], A[9]:
#           Låt summa = summa + 3*s
#   För varje siffra s = A[2], A[4], A[6], A[8]:
#           Låt summa = summa + 7*s
#   Låt kontrollsiffra = {resten när summa delas med 10}
#   Skriv ut kontrollsiffra

A = list(map(int, input().split()))

sum = 0

for i in range(9):
    if i % 2 == 0:
        sum += 3 * int(A[i])
    else:
        sum += 7 * int(A[i])

print(sum % 10)