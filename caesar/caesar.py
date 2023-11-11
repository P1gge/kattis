k = int(input())
cryp = input()

def dechif(N, k):
    if N.isalpha():
        bas = ord('a') if N.islower() else ord('A')
        dechiffra_index = (ord(N) - bas - k) % 26
        return chr(bas + dechiffra_index)
    else:
        return N

dechif = ''.join(dechif(N, k) for N in cryp)

print(dechif)