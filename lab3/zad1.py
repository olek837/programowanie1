lista=[]
while True:
    opcja=int(input("wybierz opcję "))
    if opcja ==1:
        a=int(input("pierwsza liczba "))
        b=int(input("druga liczba "))
        wynik= a+b
        lista.append("dodawanie "+str(a)+"+ "+str(b)+"= "+ str(wynik))
        print(lista)
    elif opcja ==2:
            a=int(input("pierwsza liczba "))
            b=int(input("druga liczba "))
            wynik= a-b
            lista.append("odejmowanie "+str(a)+"- "+str(b)+"= "+ str(wynik))
            print(lista)
    
    elif opcja ==5:
            a=int(input("pierwsza liczba "))
            b=int(input("druga liczba "))
            wynik= a**b
            lista.append("potęgowanie "+str(a)+"** "+str(b)+"= "+ str(wynik))
            print(lista)
    