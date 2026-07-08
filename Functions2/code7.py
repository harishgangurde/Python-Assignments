
def Max(x,y):
    if x > y:
        return x
    else:
        return y

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

maxNum = Max(num1,num2)
print("Maximum number is:",maxNum)
