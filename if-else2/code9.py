
char1 = input("Enter char1: ")
char2 = input("Enter char2: ")

sum = ord(char1) + ord(char2)

if sum % 2 == 0:
    print(sum)

else:
    print("Sum is odd")
