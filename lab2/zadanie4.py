lista =[]
powyżej=[]
for i in range(1,8):
    x=int(input('dzień'+str(i)+':'))
    lista.append(x)
średnia = sum(lista)/len(lista)
for temperatura in lista:
    if temperatura>średnia:
        powyżej.append(temperatura)
print("średnia:",średnia,"C")
print("najwyższa:",max(lista),"C")
print("najniższa:",min(lista),"C")
print("powyżej średniej:",powyżej,)
print("liczba dni:",len(powyżej),)
    
