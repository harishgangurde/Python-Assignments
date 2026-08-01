
def sum(n):
    total = 0
    i = 1

    while i <= n:
        total += i
        i += 1

    return total

num = int(input("Enter number: "))

retVal = sum(num)

print(retVal)


