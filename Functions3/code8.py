
def Prime(x):
    if x<= 1:
        return False

    i = 2
    while i < x:
        if x % i == 0:
            return False
        
        i += 1

    return True

num = int(input("Enter number: "))

if Prime(num):
    print(num,"is prime number")

else:
    print(num,"is not prime number")
