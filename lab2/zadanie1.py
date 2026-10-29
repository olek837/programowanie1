lista = []
ilość = int(input("ile produktów chcesz dodać? "))
for i in range(1,ilość+1):
    dodany = input("produkt" + str(i) + ": ")
    lista.append(dodany)
print(lista)
print("ilość produktów",len(lista))
usunięcie= input ("produkt do usunięcia:")
lista.remove(usunięcie)
print("Nowa lista",lista)
