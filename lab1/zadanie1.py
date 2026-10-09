cena = float(input("podaj cenę produktu:"))
sztuki = int(input("podaj liczbę sztuk"))
print(f"wartość zamówienia: {cena * sztuki}")
if cena * sztuki >= 100:
  print("Dostawa gratis")
  print(f"do zapłaty: {cena * sztuki}")
if cena * sztuki < 100:
    print("koszt dostawy: 12 zł")
    print(f"do zapłaty: {cena * sztuki + 12}")
