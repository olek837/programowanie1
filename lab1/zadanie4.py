wiek=int(input("podaj wiek: "))
if wiek>=18:
    dowód=input("czy masz dokument tożsamości? (tak/nie): ")
    if dowód=="tak":
        print("wypożyczenie możliwe")
    else:
        print("wypożyczenie niemożliwe")
elif wiek>=13 and wiek<18:
    zgoda=input("czy masz zgodę opiekuna? (tak/nie): ")
    dowód=input("czy masz dokument tożsamości? (tak/nie): ")
    if zgoda=="nie" or dowód=="nie":
        print("wypożyczenie niemożliwe")
    else:
        print("wypożyczenie możliwe")
else:
    print("wypożyczenie niemożliwe")
    