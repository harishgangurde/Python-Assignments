
a = 100
b = 100
list1 = [1,2,3]
list2 = [1,2,3]

print("Integer Variable:")
print(id(a))
print(id(b))

print("a is b:",a is b)
print("a is not b:",a is not b)

print("List Variable:")
print(id(list1))
print(id(list2))

print("list1 is list2:",list1 is list2)
print("list1 == list2:",list1 == list2)
print("list1 is not list2:",list1 is not list2)
