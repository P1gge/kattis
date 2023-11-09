import sys

for i in sys.stdin:
    x, y = i.split()
    print(abs(int(x)-int(y)))