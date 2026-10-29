hasło="Python123"
próby=0
pozostałe=3
while True:
    x=input("podaj hasło: ")
    if x!="Python123":
        próby+=1
        pozostałe=pozostałe-1
    if próby>=1 and próby<3 and x!="Python123":
        print("niepoprawne hasło. pozostałe próby:",pozostałe,)
    elif pozostałe==0:
        print("konto zablokowane")
        break
    else:
        print("logowanie udane!")
        break


        
