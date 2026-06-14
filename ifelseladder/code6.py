
char = input("Enter character: ")

if  'A' <= char <= 'Z':
    print("UpperCase Letter")

elif 'a' <= char <= 'z':
    print("LowerCase Letter")

elif  char.isdigit():
    print("digit")

else:
    print("Special character")
