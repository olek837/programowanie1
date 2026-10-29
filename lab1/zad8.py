k = int(input("podaj ile pieter w choince "))
for i in range(1,k+1):
    if i == 1:
        print(" " * (k-i),"*")
    else:
        print(" "*(k-i),"*" * (2*i-1))

