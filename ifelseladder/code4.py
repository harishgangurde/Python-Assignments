income = int(input("Enter income: "))

if income <= 250000:
    print("No tax")

elif 250001 < income <= 500000:
    print("Tax to be paid: ", (income - 250000) * 0.05)

elif 500001 < income <= 1000000:
    tax = (250000 * 0.05) + ((income - 500000) * 0.20)
    print("Tax to be paid: ", tax)

else:
    tax = (250000 * 0.05) + (500000 * 0.20) + ((income - 1000000) * 0.30)
    print("Tax to be paid: ", tax)

