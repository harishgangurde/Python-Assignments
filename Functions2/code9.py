
def average(*args):
    return sum(args) / len(args)

n = int(input("How many numbers do you want to enter? "))

values = []
for i in range(n):
    num = float(input(f"Enter value {i+1}: "))
    values.append(num)

avg = average(*values)

print("Average is:", avg)
