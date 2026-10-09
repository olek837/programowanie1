punkty = int(input("podaj liczbę punktów"))
if punkty >= 0 and punkty < 50:
    print(f"liczba punktów: {punkty}") 
    print("uzyskana ocena to 2")
elif punkty >=50 and punkty < 60:
    print(f"liczba punktów: {punkty}")
    print("uzyskana ocena to 3")
elif punkty >=60 and punkty <70:
    print(f"liczba punktów: {punkty}")
    print("uzyskana ocena to 3.5")
elif punkty >=70 and punkty <80:
    print(f"liczba punktów: {punkty}")
    print("uzyskana ocena to 4")
elif punkty >=80 and punkty <90:
    print(f"liczba punktów: {punkty}")
    print("uzyskana ocena to 4.5")
elif punkty >=90 and punkty <= 100:
    print(f"liczba punktów: {punkty}")
    print("uzyskana ocena to 5")
else:
    print("błędne dane")