
def Avgmarks():
    total = 0
    i = 1
    while i <= 5:
        marks = int(input("Enter marks: "))
        total += marks
        i += 1

    return total / 5

retVal = Avgmarks()
print(retVal)
