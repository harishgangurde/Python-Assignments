

age = int(input("Enter age: "))
weight = int(input("Enter weight: "))
Hb = float(input("Enter hb: "))

if 18 <= age <=65 and weight > 50 and Hb > 12.5:
    print("Eligible for blood donation")


else:
    print("Not eligible for blood donation")
