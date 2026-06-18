
angle1 = int(input("Enter angle1: "))
angle2 = int(input("Enter angle2: "))
angle3 = int(input("Enter angle3: "))

sum = angle1 + angle2 + angle3
if 90 < angle1 < 180 and 90 < angle2 < 180 and 90 < angle3 < 180 and sum == 180 :
    print("Triangle is Obtuse angle")

elif angle1 < 90 and angle2 < 90 and angle3 < 90 and sum == 180 :
    print("triangle is Acute angle")

else:
    print("Invalid triangle")
