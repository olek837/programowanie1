liczba = int(input("podaj liczbę studentów: "))
zaliczeni = 0
for i in range(1, liczba + 1):
    nazwisko = input("podaj nazwisko studenta: ")
    punkty = int(input("podaj liczbę punktów: "))
    if punkty >=0 and punkty < 50:
        print("student",nazwisko,"nie zaliczył")
    elif punkty >=50 and punkty <60:
        print("student",nazwisko,"zaliczył na ocenę 3.0")
        zaliczeni += 1
    elif punkty >=60 and punkty <70:
        print("student",nazwisko,"zaliczył na ocenę 3.5")
        zaliczeni += 1
    elif punkty >=70 and punkty <80:
        print("student",nazwisko,"zaliczył na ocenę 4.0")
        zaliczeni += 1
    elif punkty >=80 and punkty <90:
        print("student",nazwisko,"zaliczył na ocenę 4.5")
        zaliczeni += 1
    elif punkty >=90 and punkty <=100:
        print("student",nazwisko,"zaliczył na ocenę 5.0")
        zaliczeni += 1
    else:
        print("nieprawidłowa liczba punktów")
print("liczba studentów, którzy zaliczyli:", zaliczeni)

