
def vote(x):
    if x < 18:
        print("Not eligible for voting")
    else:
        print("Eligible for voting")

age = int(input("Enter age: "))

vote(age)
