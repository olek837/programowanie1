historia = []

while True:
    print("\n========== KALKULATOR ==========")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnozenie")
    print("4. Dzielenie")
    print("5. Potegowanie")
    print("6. Srednia z podanych liczb")
    print("0. Zakoncz")
    print("================================")

    opcja = input("Wybierz opcje: ")

    if opcja == "1":
        a = float(input("Pierwsza liczba: "))
        b = float(input("Druga liczba: "))
        wynik = a + b

        dzialanie = f"{a} + {b} = {wynik}"
        print("Wynik:", dzialanie)
        historia.append(dzialanie)

    elif opcja == "2":
        a = float(input("Pierwsza liczba: "))
        b = float(input("Druga liczba: "))
        wynik = a - b

        dzialanie = f"{a} - {b} = {wynik}"
        print("Wynik:", dzialanie)
        historia.append(dzialanie)

    elif opcja == "3":
        a = float(input("Pierwsza liczba: "))
        b = float(input("Druga liczba: "))
        wynik = a * b

        dzialanie = f"{a} * {b} = {wynik}"
        print("Wynik:", dzialanie)
        historia.append(dzialanie)

    elif opcja == "4":
        a = float(input("Pierwsza liczba: "))
        b = float(input("Druga liczba: "))

        if b == 0:
            print("Nie mozna dzielic przez zero.")
        else:
            wynik = a / b
            dzialanie = f"{a} / {b} = {wynik}"
            print("Wynik:", dzialanie)
            historia.append(dzialanie)

    elif opcja == "5":
        a = float(input("Pierwsza liczba: "))
        b = float(input("Druga liczba: "))
        wynik = a ** b

        dzialanie = f"{a} ** {b} = {wynik}"
        print("Wynik:", dzialanie)
        historia.append(dzialanie)

    elif opcja == "6":
        ile = int(input("Ile liczb? "))

        if ile <= 0:
            print("Liczba elementow musi byc dodatnia.")
        else:
            liczby = []

            for i in range(1, ile + 1):
                liczba = float(input("Liczba " + str(i) + ": "))
                liczby.append(liczba)

            srednia = sum(liczby) / ile
            print("Srednia:", srednia)

            dzialanie = f"Srednia z {liczby} = {srednia}"
            historia.append(dzialanie)

    elif opcja == "0":
        break

print("Historia dzialan:")
for dzialanie in historia:
    print(dzialanie)

print("Do widzenia!")