nombre = int(input("entrez un nombre : "))
limite = int(input("entrez un nombre limite : "))
for i in range (limite + 1):
    print(f"{nombre} X {i} = {nombre*i}")