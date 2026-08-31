
def Fac(n):
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    return factorial

num = int(input("Enter number: "))
retVal = Fac(num)

print("Factorial is:",retVal)

