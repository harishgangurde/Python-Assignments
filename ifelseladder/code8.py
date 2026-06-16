
num = int(input("Enter number: "))

if num == 0:
    print("Zero")

elif num > 0:
    if num % 2 == 0:
        print("Positive Even")

    elif num % 2 == 1:
        print("Positive Odd")

elif num < 0:
    if num % 2 == 0:
        print("Negative Even")
    
    else:
        print("Negative Odd")
