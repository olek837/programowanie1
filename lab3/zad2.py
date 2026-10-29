
kontakty = {}

while True:
    print("========== KSIAZKA KONTAKTOW ==========")
    print("1. Dodaj kontakt")
    print("2. Wyswietl wszystkie kontakty")
    print("3. Wyszukaj kontakt")
    print("4. Edytuj kontakt")
    print("5. Usun kontakt")
    print("0. Zakoncz")
    print("=======================================")

    opcja = input("Wybierz opcje: ")

    if opcja == "1":
        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        telefon = input("Telefon: ")

        if telefon in kontakty:
            print("Kontakt o tym numerze juz istnieje.")
        else:
            kontakty[telefon] = [imie, nazwisko]
            print("Kontakt dodany.")

    elif opcja == "2":
        if not kontakty:
            print("Ksiazka kontaktow jest pusta.")
        else:
            for telefon, dane in kontakty.items():
                print(dane[0], dane[1], "- telefon:", telefon)

    elif opcja == "3":
        telefon = input("Podaj numer telefonu: ")

        if telefon in kontakty:
            dane = kontakty[telefon]
            print(dane[0], dane[1], "- telefon:", telefon)
        else:
            print("Nie znaleziono kontaktu.")

    elif opcja == "4":
        telefon = input("Podaj numer telefonu kontaktu do edycji: ")

        if telefon in kontakty:
            imie = input("Nowe imie: ")
            nazwisko = input("Nowe nazwisko: ")
            kontakty[telefon] = [imie, nazwisko]
            print("Kontakt zaktualizowany.")
        else:
            print("Nie znaleziono kontaktu.")

    elif opcja == "5":
        telefon = input("Podaj numer telefonu kontaktu do usuniecia: ")

        if telefon in kontakty:
            del kontakty[telefon]
            print("Kontakt usuniety.")
        else:
            print("Nie znaleziono kontaktu.")

    elif opcja == "0":
        print("Do widzenia!")
        break

    else:
        print("Nieprawidlowa opcja.")
    
