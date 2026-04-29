
angle1 = int(input("Enter angle1: "))
angle2 = int(input("Enter angle2: "))
angle3 = int(input("Enter angle3: "))

if ((angle1 == 90 or angle2 == 90 or angle3 == 90) and (angle1 + angle2 +angle3) == 180):
    print("It is a right angle triangle")

else:
    print("It is not right angle triangle")
