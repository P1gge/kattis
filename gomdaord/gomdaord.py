kryp = input()
pos = 0
save = ""

while pos < len(kryp):
    save += kryp[pos]
    pos += (ord(kryp[pos]) - 64)

print(save)