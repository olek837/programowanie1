budżet={}
while True:
    print("=====Mój budżet======")
    print("1.Dodaj przychód")
    print("2.dodaj wydatek")
    print("3.wyświetl historię operacji")
    print("4.wyświetl stan konta")
    print("5.podsumowanioe finansowe")
    print("6.usuń operację")
    print("0.zakończ")
    print("==========================")
    x = int(input("wybierz opcję"))
    if x==1:
        opis=input("opis: ")
        kwota= int(input("Kwota: "))
        if kwota > 0:
            budżet[opis,"PRZYCHÓD"]=kwota
            print("dodano przychód")
        elif x<0:
            print("kwota musi być większa od zera")
    elif x==2:
        opis =input("opis: ")
        kwota = int(input("Kwota: "))
        if kwota>0:
            budżet[opis,"wydatek"]=-kwota
            print("dodano wydatek")
        if kwota<0:
            print("podaj kwotę większą od zera")
    elif x==3:
        print(budżet)
    elif x==4:
        suma=0
        for opis in budżet:
            suma = suma + budżet[opis]
            print("stan konta wynosi:",suma)
    
    
