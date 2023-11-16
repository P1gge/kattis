str_input = input()

konsonant = "bcdfghjklmnpqrstvwxz"
lista = []

for i in str_input:
    if i in konsonant:
        if len(lista) < 2 or (i != lista[-1] or i != lista[-2]):
            lista.append(i)
    else:
        lista.append(i)

print(''.join(lista))