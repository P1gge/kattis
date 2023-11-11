cap = list(map(int, input().split()))
stu = int(input())

if stu >= cap[0]:
    print("A")
elif stu >= cap[1]:
    print("B")
elif stu >= cap[2]:
    print("C")
elif stu >= cap[3]:
    print("D")
elif stu >= cap[4]:
    print("E")
else:
    print("F")