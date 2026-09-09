def is_composite(n):
    if n <= 1:
        return False

    i = 2
    while i < n:
        if n % i == 0:  
            return True
        i += 1

    return False
num = int(input("Enter a number: "))

if is_composite(num):
    print(num, "is a composite number")
else:
    print(num, "is not a composite number")
