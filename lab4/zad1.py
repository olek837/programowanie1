lista =[]
x=int(input("ile pomiarów: "))
for i in range(1,x+1):
    y=int(input("pomiar "+str(i)+": "))
    lista.append(y)
print("pierwszy pomiar: ",lista[1])
print("ostatni pomiar: ",lista[-1])
print("trzy pierwsze pomiary: ",lista[:3])
print("co drugi pomiar: ",lista[::2])
print("odwrotna kolejność")
    