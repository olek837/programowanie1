temperatura = float(input('podaj temperaturę: '))
osoby = input('czy któś jest w domu? (tak/nie): ')
okno = input('czy okno jest otwarte? (tak/nie): ')
if okno == "tak":
    print("ogrzewanie: WYŁĄCZONE")
    print('Powód: okno jest otwarte')
elif okno== "nie" and osoby == "tak"and temperatura < 20:
    print("ogrzewanie: WŁĄCZONE")
    print('Powód: w domu są osoby i temperatura jest niższa niż 20 stopni')
elif okno== "nie" and osoby == "nie" and temperatura < 16:
    print("ogrzewanie: WŁĄCZONE")
    print('Powód: w domu nie ma osób i temperatura jest niższa niż 16 stopni')
else:
    print("ogrzewanie: WYŁĄCZONE") 
    print('Powód: nie spełnione są warunki dla włączenia ogrzewania')