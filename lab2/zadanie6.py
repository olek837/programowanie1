lista=[]
print("1-dodaj zadanie")
print("2-wyświetl zadania")
print("3-usuń zadanie")
print("4-liczba zadań")
print("0-zakończ")
while True:
    x=int(input("wybierz opcję: "))
    if x ==1:
        y=input("podaj zadanie: ")
        lista.append(y)
    elif x==2:
        print(lista)
    elif x==3:
        zadanie=int(input('podaj numer zadania: '))
        lista.pop(zadanie-1)
        print('zadanie usunięte')
    elif x==4:
        print("liczba zadań wynosi:",len(lista))
    elif x==0:
        print("do widzenia!")
        break

