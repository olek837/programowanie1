cena = float(input("podaj cene produktu: "))
rabat = float(input("podaj rabat %: "))
print(f"cena początkowa: {cena} zł")
print(f"rabat: {cena*rabat/100}zł")
print(f"cena po rabacie: {cena*(1-rabat/100)} zł")
if cena*(1-rabat/100) <= 0.8*cena:
    print("duża promocja!") 
else:
    print("standardowa promocja")



