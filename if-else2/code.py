
x = int(input("Enter Height: "))
y = int(input("Enter base: "))
z = int(input("Enter Hypotenous: "))

if ((x**2) + (y**2) == (z**2)) or ((x**2) + (z**2) == (y**2)) or ((y**2) + (z**2) == (x**2)) :
    print("yes it is pythogorean triplet")

else:
    print("No it is not a pythogorean triplet")
