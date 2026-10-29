lista ={}
while True:
        print("========== KSIAZKA KONTAKTOW ==========")
        print("1. Dodaj kontakt")
        print("2. Wyswietl wszystkie kontakty")
        print("3. Wyszukaj kontakt")
        print("4. Edytuj kontakt")
        print("5. Usun kontakt")
        print("0. Zakoncz")
        print("=======================================")
        x=int(input("wybierz opcję: "))
        if x==1:
            imie=input('podaj imię: ')
            nazwisko=input("podaj nazwisko: ")
            tel=int(input("podaj numer telefonu: "))
            if tel in lista:
                  print("ten numer już istnieje")
            else:
                  lista[tel]=[imie,nazwisko]
                  print("kontakt dodany")
        elif x ==2:
              if not lista:
                    print("słownik jest pusty")
              else:
                    print(lista)
        elif x==3:
              numer=int(input("podaj numer tel: "))
              if numer in lista:
                    print(lista[numer])
              else:
                    print("nie ma takiego kontaktu")
        elif x==4:
              numer=int(input("podaj numer "))
              imię=input("podaj imię ")
              nazwisko=input("nazwisko ")
              if numer in lista:
                    lista[numer]=[imię,nazwisko]
                    print("kontakt zmieniony")
              else:
                    print("nie ma takiego numeru")
        elif x ==5:
              numer=int(input("numer "))
              del lista[numer]
        elif x == 0:
              break
              print("do widzenia")



    