
x = input("Enter Character: ")

if len(x) == 1:
    
    if x == 'a' or x=='e' or x=='i' or x=='o' or x=='u' or x == 'A' or x=='E' or x=='I' or x=='O' or x=='U':
        print("Vowel")

    elif 'a'<= x <= 'z' or 'A' <= x <= 'Z':
        print(x,"is a special character ")

    else:
        print("Consonant")

else:
    print(x,"Not a character")
