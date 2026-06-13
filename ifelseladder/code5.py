
temp = int(input("Enter temperature: "))

if temp < 0:
    print("Freezing cold")

elif 0 <= temp <= 10:
    print("Very cold")
elif 11 <= temp <= 20:
    print("Cold")
elif 21 <= temp <= 30:
    print("warm")
elif 31 <= temp <= 40:
    print("Very cold")
else:
    print("Extreme Heat")
