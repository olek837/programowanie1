zakres1  = int(input("Podaj początek zakresu: "))
zakres2  = int(input("Podaj koniec zakresu: "))
parzyste = 0
for i in range(zakres1, zakres2  + 1):
    if i % 2==0:
        print( (i)," - parzysta")
        parzyste += 1
    if i%2 == 1:
        print( (i), " - nieparzysta")
print("liczba liczb parzystych: ", parzyste)




