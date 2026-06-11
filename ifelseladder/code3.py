
units = int(input("Enter unit: "))

if units == 100:
    print("Total Bill: ",units*5)
elif 101 <= units <= 200:
    print("Total bill: ",units*7)
elif 201 <= units <= 300:
    print("Total bill: ",units*10)
else:
    print("Total bill: ",units*15)
