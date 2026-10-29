napoje = ["woda","sok","cola"]
ceny=[3,5,6]
for i in range(3):
    print(napoje[i],"-",ceny[i],"zł")
print("0. Zakończ")
cena=0
while True:
    x = int(input("wybierz  opcję: "))
    opcja = x - 1
    print(napoje[opcja]," cena:", ceny[opcja],"zł",)
    if x>=1 and x<=3:
        cena = cena + ceny[opcja]
    elif x==0:
        break
print('łącznie do zapłaty:',cena,"zł")






