
def Operations(x,y):
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    mod = x % y
    rem = x // y
    return add,sub,mul,div,mod,rem

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

ans = Operations(num1,num2)
for i in ans:
    print(i)
