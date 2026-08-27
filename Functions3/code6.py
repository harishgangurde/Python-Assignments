
def prod(n):
    product = 1
    i = 1
    while i <= n:
        product = product * i
        i += 1

    return product

num = int(input("Enter number: "))

retVal = prod(num)

print("Product is:",retVal)
