I = input()
a, b, c = map(int, I.split())
list = [a, b, c]
list.sort()
for i in list:
    print(i, end=" ")