liczba = int(input("podaj liczbę studentów "))
lista=[]
zdający=0
for i in range(1,liczba+1):
    student=int(input("student"+str(i)+":"))
    lista.append(student)
    if student>=50:
        zdający+=1
x=sum(lista)/len(lista)

print("średnia: ",x)
print("najwyższy wynik:",max(lista))
print("najniższy wynik:",min(lista))
print(sorted(lista))
print("liczba zaliczeń:",zdający)






   
    