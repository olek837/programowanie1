magazyn={"Mysz":5,"Klawiatura":3,"monitor":2}
print("1. Stan magazynu")
print("2. przyjęcie towaru")
print("3. wydanie towaru")
print("0. zakończ")
while True:
    x=int(input("wybierz opcję: "))
    if x==1:
        print(magazyn)
    elif x==2:
        y=input("nazwa produktu: ")
        z=int(input("liczba sztuk: "))
        if y in magazyn:
            magazyn[y]=magazyn[y] + z 
        else:
            magazyn[y]=z
        print("zaktualizowano stan produktu")
    elif x ==3:
        nazwa=input("nazwa produktu: ")
        liczba=int(input("liczba sztuk: "))
        if nazwa in magazyn:
            if liczba <= magazyn[nazwa]:
                magazyn[nazwa]=magazyn[nazwa]-liczba
            else:
                print("nie ma tyle sztuk")
        else:
            print("nie ma takiego produktu")
    elif x == 0:
        print("do widzenia!")
        break

