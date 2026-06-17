
amount = float(input("Enter purchase amount: "))

if amount < 1000:
    discount = 0
elif amount <= 4999:
    discount = 0.05
elif amount <= 9999:
    discount = 0.10
elif amount <= 19999:
    discount = 0.20
else:
    discount = 0.30

final_amount = amount - (amount * discount)

print("Discount Applied:", int(discount * 100), "%")
print("Final Amount: ₹", final_amount)
