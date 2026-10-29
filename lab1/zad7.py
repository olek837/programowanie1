kwota=float(input("ile odkładasz tygodniowo?: "))
tygodnie = int(input("przez ile tygodni?: "))
for i in range(1,tygodnie+1):
    print(f"tydzień {i}: {kwota*i}zł")
print(f"łączne oszczędności to: {kwota*tygodnie}zł")
