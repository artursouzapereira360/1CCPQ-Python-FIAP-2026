lista_duplas =  ["Ana", "Maria", "Enzo", "Leo"]

print(lista_duplas)

for i in (range(len(lista_duplas))):
    for j in (range(i + 1, len(lista_duplas))):
        print(lista_duplas[i], "-", lista_duplas[j])
