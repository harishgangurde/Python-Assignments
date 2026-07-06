
def vowel(x):
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
        print(x,"is vowel")
    else:
        print(x,"is consonant")

char = input("Enter character: ")

vowel(char)
