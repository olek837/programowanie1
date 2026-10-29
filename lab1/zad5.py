czas=int(input("podaj czas parkowania (h): "))
print(f"czas postoju wtnosi: {czas}h")
if czas == 1:
    print("opłata za parking: 5 zł")
elif czas >1 and czas <=3:
    print("opłata za parking: 12zł")
elif czas>3 and czas <=6:
    print("opłata za parking: 20zł")
elif czas>6:
    print("opłata za parking: 30zł")
else:
    print("nieprawidłowe dane")